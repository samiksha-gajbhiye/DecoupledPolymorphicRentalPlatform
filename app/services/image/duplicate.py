from __future__ import annotations

from io import BytesIO
from typing import Any

import imagehash
from PIL import Image

from app.config.logger import logger
from app.config.settings import settings
from app.utils.image_utils import convert_to_rgb


class DuplicateDetector:
    """Detect visually similar images using perceptual hashing.

    The detector uses pHash (perceptual hashing) to compare images.
    Smaller Hamming distances indicate greater visual similarity.

    compare() is the main public method. No AI model is loaded,
    so there is no model initialization or warmup required.
    """

    def __init__(
        self,
        threshold: int | None = None,
        hash_size: int = 8,
    ) -> None:
        """Initialize the duplicate detector.

        Args:
            threshold:
                Maximum Hamming distance for two images to be
                considered duplicates. If omitted, the value from
                settings.ai.duplicate_threshold is used.

            hash_size:
                Size of the perceptual hash. The default 8 produces
                an 8x8 hash containing 64 bits.
        """

        if threshold is not None and threshold < 0:
            raise ValueError(
                "Duplicate threshold cannot be negative."
            )

        if hash_size <= 0:
            raise ValueError(
                "Hash size must be greater than zero."
            )

        self.threshold = (
            threshold
            if threshold is not None
            else settings.ai.duplicate_threshold
        )

        self.hash_size = hash_size

        logger.info(
            "DuplicateDetector initialized "
            "with threshold=%d, hash_size=%d",
            self.threshold,
            self.hash_size,
        )

    def compare(
        self,
        image_a: Image.Image | bytes | BytesIO,
        image_b: Image.Image | bytes | BytesIO,
    ) -> dict[str, float | int | bool]:
        """Compare two images for visual similarity.

        Args:
            image_a:
                First image as PIL Image, raw bytes, or BytesIO.

            image_b:
                Second image as PIL Image, raw bytes, or BytesIO.

        Returns:
            Dictionary containing:

            - distance: Hamming distance between perceptual hashes.
            - similarity: Normalized similarity score between 0 and 1.
            - is_duplicate: Whether the distance is within the threshold.
            - threshold: Threshold used for the comparison.
        """

        validated_a = self._validate_image(image_a)
        validated_b = self._validate_image(image_b)

        hash_a = self._calculate_hash(validated_a)
        hash_b = self._calculate_hash(validated_b)

        distance = self._calculate_distance(
            hash_a,
            hash_b,
        )

        similarity = self._calculate_similarity(
            distance,
            hash_a,
        )

        is_duplicate = distance <= self.threshold

        result = {
            "distance": distance,
            "similarity": similarity,
            "is_duplicate": is_duplicate,
            "threshold": self.threshold,
        }

        logger.debug(
            "Duplicate comparison completed: "
            "distance=%d, similarity=%.4f, duplicate=%s",
            distance,
            similarity,
            is_duplicate,
        )

        return result

    def _validate_image(
        self,
        image: Image.Image | bytes | BytesIO,
    ) -> Image.Image:
        """Validate and normalize an image into RGB PIL format.

        Supported inputs:
            - PIL.Image.Image
            - bytes
            - BytesIO
        """

        if isinstance(image, bytes):
            image = BytesIO(image)

        if isinstance(image, BytesIO):
            try:
                image = Image.open(image)
                image.load()
            except Exception as exc:
                raise ValueError(
                    "Unable to read image data."
                ) from exc

        if not isinstance(image, Image.Image):
            raise TypeError(
                "Expected PIL.Image, bytes, or BytesIO."
            )

        return convert_to_rgb(image)

    def _calculate_hash(
        self,
        image: Image.Image,
    ) -> imagehash.ImageHash:
        """Calculate the perceptual hash of an image.

        pHash is intentionally used instead of a cryptographic
        hash because visually similar images can have different
        file bytes while still producing similar perceptual hashes.
        """

        return imagehash.phash(
            image,
            hash_size=self.hash_size,
        )

    def _calculate_distance(
        self,
        hash_a: imagehash.ImageHash,
        hash_b: imagehash.ImageHash,
    ) -> int:
        """Calculate the Hamming distance between two hashes.

        A smaller distance means the images are more visually similar.
        """

        return int(hash_a - hash_b)

    def _calculate_similarity(
        self,
        distance: int,
        hash_a: imagehash.ImageHash,
    ) -> float:
        """Normalize Hamming distance into a 0-1 similarity score.

        This is a normalized similarity metric, not a probability.
        For example, 0.97 does not mean there is a 97% probability
        that the images are duplicates.
        """
        hash_size_bits = hash_a.hash.size
        similarity = max(
            0.0,
            1.0 - (
                distance / hash_size_bits
            ),
        )
        return round(
            similarity,
            4,
        )
__all__ = ("DuplicateDetector",)