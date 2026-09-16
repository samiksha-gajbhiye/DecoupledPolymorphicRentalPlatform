from __future__ import annotations

from fastapi import HTTPException, UploadFile, status

from app.config.logger import logger
from app.schemas.response import DetectData, DetectResponse
from app.services.image.detector import ImageDetector
from app.utils.image_utils import load_image


class ImageDetectionService:
    """One-shot YOLO object detection. No database, no disk writes."""

    _detector = ImageDetector()

    async def detect(self, file: UploadFile) -> DetectResponse:
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
            result = self._detector.detect(image)
        except Exception as exc:
            logger.exception("Detection failed.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Image detection failed.",
            ) from exc

        logger.info(f"Detected {result['object_count']} object(s) in filename={file.filename}")

        return DetectResponse(
            success=True,
            message="OK",
            data=DetectData(**result),
        )


__all__ = ("ImageDetectionService",)