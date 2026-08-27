from __future__ import annotations

import string
from io import BytesIO

import imagehash
from fastapi import HTTPException, UploadFile, status

from app.config.logger import logger
from app.schemas.response import (
    HashCompareData,
    HashCompareResponse,
    HashData,
    HashMatchResult,
    HashResponse,
)
from app.services.image.duplicate import DuplicateDetector


class ImageHashService:
    """Stateless perceptual hashing. No database, no disk writes.

    Duplicate detection is split into two independent steps so that
    neither one needs to look anything up:

    - compute_hash: one image in, one hash string out.
    - compare_hashes: hash strings in, distances out. No images at all.

    Java owns the remembering — it stores each hash and decides which
    ones a new upload gets compared against.
    """

    # Shared instance: DuplicateDetector loads no model, but this keeps
    # threshold/hash_size consistent across every request.
    _detector = DuplicateDetector()

    # phash with hash_size=8 produces 64 bits, which is 16 hex characters.
    _HEX_DIGITS = frozenset(string.hexdigits)

    @property
    def _expected_hash_length(self) -> int:
        return self._detector.hash_size**2 // 4

    async def compute_hash(self, file: UploadFile) -> HashResponse:
        raw_bytes = await file.read()
        if not raw_bytes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty.",
            )

        # Deliberately reuses the detector's own validate + hash steps so a
        # hash from this endpoint is always comparable with one produced
        # anywhere else in the project.
        try:
            image = self._detector._validate_image(BytesIO(raw_bytes))
        except (ValueError, TypeError) as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is not a valid image.",
            ) from exc

        try:
            image_hash = self._detector._calculate_hash(image)
        except Exception as exc:
            logger.exception("Failed to compute perceptual hash.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to compute image hash.",
            ) from exc

        hash_hex = str(image_hash)

        logger.info(
            f"Computed perceptual hash filename={file.filename} "
            f"hash={hash_hex} hash_size={self._detector.hash_size}"
        )

        return HashResponse(
            success=True,
            message="OK",
            data=HashData(
                hash=hash_hex,
                hash_size=self._detector.hash_size,
            ),
        )

    async def compare_hashes(
        self,
        target_hash: str,
        candidate_hashes: list[str],
    ) -> HashCompareResponse:
        target = self._parse_hash(target_hash, label="target_hash")

        results: list[HashMatchResult] = []
        for raw_candidate in candidate_hashes:
            candidate = self._parse_hash(raw_candidate, label="candidate_hashes")

            distance = self._detector._calculate_distance(target, candidate)
            similarity = self._detector._calculate_similarity(distance, target)

            results.append(
                HashMatchResult(
                    candidate_hash=str(candidate),
                    distance=distance,
                    similarity=similarity,
                    is_duplicate=distance <= self._detector.threshold,
                )
            )

        duplicate_count = sum(1 for result in results if result.is_duplicate)
        logger.info(
            f"Compared target hash against {len(results)} candidate(s), "
            f"{duplicate_count} duplicate(s) found"
        )

        return HashCompareResponse(
            success=True,
            message="OK",
            data=HashCompareData(
                threshold=self._detector.threshold,
                results=results,
            ),
        )

    def _parse_hash(self, value: str, label: str) -> imagehash.ImageHash:
        """Turn a hex string back into an ImageHash, or fail with a clear 400.

        Length is checked explicitly rather than left to imagehash: a
        wrong-length string still decodes, but into a different grid shape,
        and subtracting mismatched shapes raises a confusing ValueError
        later instead of naming the bad input here.
        """

        cleaned = value.strip().lower()
        expected = self._expected_hash_length

        if len(cleaned) != expected:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    f"Invalid {label}: expected {expected} hex characters "
                    f"for hash_size={self._detector.hash_size}, got {len(cleaned)}."
                ),
            )

        if not set(cleaned) <= self._HEX_DIGITS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid {label}: '{value}' is not a valid hex string.",
            )

        try:
            return imagehash.hex_to_hash(cleaned)
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid {label}: '{value}' could not be decoded as a perceptual hash.",
            ) from exc


__all__ = ("ImageHashService",)
