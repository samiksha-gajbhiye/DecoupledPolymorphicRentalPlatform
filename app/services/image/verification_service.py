from __future__ import annotations
 
from io import BytesIO
 
from fastapi import HTTPException, UploadFile, status
from PIL import Image
 
from app.config.logger import logger
from app.schemas.response import VerifyData, VerifyResponse
from app.services.image.blur_detection import BlurDetector
from app.services.image.classifier import ImageClassifier
 
 
class ImageVerificationService:
    """One-shot classify + blur check. No database, no disk writes."""
 
    # Loaded once per process, not per request — CLIP-style model loads are
    # expensive, so they must not happen inside a request handler.
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
            image = Image.open(BytesIO(raw_bytes))
            image.load()
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is not a valid image.",
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
                image_format=(image.format or "UNKNOWN").upper(),
                file_size=len(raw_bytes),
                matches_expected=matches_expected,
            ),
        )
 
 
__all__ = ("ImageVerificationService",)