from __future__ import annotations

from fastapi import HTTPException, UploadFile, status

from app.config.logger import logger
from app.schemas.response import VerifyData, VerifyResponse
from app.services.image.blur_detection import BlurDetector
from app.services.image.classifier import ImageClassifier
from app.utils.image_utils import load_image

# Maps known-misspelled/variant category names (as they actually exist in
# Java's category table) to the correctly-spelled classifier category they
# mean. Add an entry here whenever a mismatch like this is confirmed --
# this is a data-entry problem, not something worth building fuzzy-matching
# for.
CATEGORY_ALIASES: dict[str, str] = {
    "electrical appliences": "electrical appliances",
    "vehical": "vehicles",
}


class ImageVerificationService:
    """One-shot classify + blur check. No database, no disk writes."""

    _classifier = ImageClassifier()
    _blur_detector = BlurDetector()

    async def verify(self, file: UploadFile, expected_category: str | None = None) -> VerifyResponse:
        raw_bytes = await file.read()
        if not raw_bytes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty.",
            )

        try:
            image = load_image(raw_bytes)
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(exc),
            ) from exc

        try:
            classification = self._classifier.classify(image)
            blur_result = self._blur_detector.detect(image)
        except Exception as exc:
            logger.exception("Verification failed while running AI checks.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Image verification failed.",
            ) from exc

        logger.info(
            f"Verified image filename={file.filename} "
            f"label={classification['label']} "
            f"category_confidence={classification['category_confidence']:.4f} "
            f"blurry={blur_result['is_blurry']}"
        )

        matches_expected = None
        if expected_category:
            expected = expected_category.strip().lower()
            expected = CATEGORY_ALIASES.get(expected, expected)
            matches_expected = expected in (classification["label"].lower(), classification["category"].lower())

        return VerifyResponse(
            success=True,
            message="OK",
            data=VerifyData(
                label=classification["label"],
                category=classification["category"],
                confidence=classification["confidence"],
                category_confidence=classification["category_confidence"],
                is_blurry=blur_result["is_blurry"],
                blur_score=blur_result["blur_score"],
                width=image.width,
                height=image.height,
                image_format="JPEG",
                file_size=len(raw_bytes),
                matches_expected=matches_expected,
            ),
        )


__all__ = ("ImageVerificationService",)