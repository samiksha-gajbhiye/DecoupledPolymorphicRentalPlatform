from __future__ import annotations
 
import uuid
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
 
from fastapi import HTTPException, UploadFile, status
from PIL import Image
from sqlalchemy.orm import Session
 
from app.config.logger import logger
from app.config.settings import settings
from app.models.image import ImageAnalysis, ProcessingStatus
from app.schemas.response import DuplicateData, DuplicateResponse, ImageData, ImageResponse
from app.services.image.blur_detection import BlurDetector
from app.services.image.classifier import ImageClassifier
from app.services.image.compressor import ImageCompressor
from app.services.image.duplicate import DuplicateDetector
 
 
class ImageService:
    """Coordinates upload, storage, AI processing, and retrieval of image analyses."""

    # Loaded once per process, not per request — CLIP/YOLO-style model
    # loads are expensive. Swap for shared/cached singletons via DI later.
    _classifier = ImageClassifier()
    _duplicate_detector = DuplicateDetector()
    _blur_detector = BlurDetector()
    _compressor = ImageCompressor()
 
    def __init__(self, db: Session) -> None:
        self.db = db
 
    # ------------------------------------------------------------------
    # Upload
    # ------------------------------------------------------------------
    async def upload_image(
        self,
        file: UploadFile,
        product_id: int | None,
    ) -> ImageResponse:
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
 
        image_format = (image.format or "UNKNOWN").upper()
        ext = (image_format or "jpg").lower()
        if ext not in settings.upload.allowed_image_formats:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Image format '{ext}' is not allowed.",
            )
 
        if len(raw_bytes) > settings.upload.max_image_size:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Image exceeds the maximum allowed size.",
            )
 
        stored_path = self._save_to_disk(raw_bytes, ext)
 
        record = ImageAnalysis(
            product_id=product_id or 0,
            image_url=str(stored_path),
            filename=file.filename or "unknown",
            width=image.width,
            height=image.height,
            image_format=image_format,
            file_size=len(raw_bytes),
            processing_status=ProcessingStatus.PENDING,
        )
 
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
 
        logger.info(f"Created image analysis record id={record.id} path={stored_path}")
        return self._to_response(record)
 
    @staticmethod
    def _save_to_disk(raw_bytes: bytes, ext: str) -> Path:
        upload_dir = settings.upload.upload_directory
        upload_dir.mkdir(parents=True, exist_ok=True)
 
        filename = f"{uuid.uuid4().hex}.{ext}"
        destination = upload_dir / filename
        destination.write_bytes(raw_bytes)
 
        return destination
 
    # Processing
    async def process_image(self, analysis_id: int) -> ImageResponse:
        record = self._get_or_404(analysis_id)
 
        if not record.image_url:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No stored image available for this analysis.",
            )
 
        stored_path = Path(record.image_url)
        if not stored_path.exists():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Stored image file is missing on disk.",
            )
 
        record.processing_status = ProcessingStatus.PROCESSING
        self.db.commit()
 
        started_at = datetime.now(timezone.utc)
 
        try:
            image = Image.open(stored_path)
            image.load()
 
            classification = self._classifier.classify(image)
            blur_result = self._blur_detector.detect(image)
 
            record.confidence = classification["confidence"]
            record.blur_score = blur_result["blur_score"]
            record.processing_status = ProcessingStatus.COMPLETED
            record.processed_at = datetime.now(timezone.utc)
            record.processing_time = (
                record.processed_at - started_at
            ).total_seconds()
            record.error_message = None
 
            self.db.commit()
            self.db.refresh(record)
 
            logger.info(
                f"Processed analysis id={analysis_id} "
                f"label={classification['label']} blurry={blur_result['is_blurry']}"
            )
            return self._to_response(record)
 
        except Exception as exc:
            record.processing_status = ProcessingStatus.FAILED
            record.error_message = str(exc)
            self.db.commit()
            logger.exception(f"Processing failed for analysis id={analysis_id}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Image processing failed.",
            ) from exc
 
    # Duplicate comparison
    async def compare_images(self, image_id_a: int, image_id_b: int) -> DuplicateResponse:
        record_a = self._get_or_404(image_id_a)
        record_b = self._get_or_404(image_id_b)
 
        for record in (record_a, record_b):
            if not record.image_url or not Path(record.image_url).exists():
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Stored image file is missing for analysis id={record.id}.",
                )
 
        image_a = Image.open(Path(record_a.image_url))
        image_b = Image.open(Path(record_b.image_url))
 
        result = self._duplicate_detector.compare(image_a, image_b)
 
        logger.info(
            f"Compared analysis ids {image_id_a} vs {image_id_b}: "
            f"distance={result['distance']} is_duplicate={result['is_duplicate']}"
        )
 
        return DuplicateResponse(
            success=True,
            message="OK",
            data=DuplicateData(**result),
        )
 
    # ------------------------------------------------------------------
    # Retrieval / deletion
    # ------------------------------------------------------------------
    async def get_analysis(self, analysis_id: int) -> ImageResponse:
        record = self._get_or_404(analysis_id)
        return self._to_response(record)
 
    async def delete_analysis(self, analysis_id: int) -> None:
        record = self._get_or_404(analysis_id)
 
        if record.image_url:
            stored_path = Path(record.image_url)
            if stored_path.exists():
                stored_path.unlink(missing_ok=True)
 
        self.db.delete(record)
        self.db.commit()
        logger.info(f"Deleted image analysis id={analysis_id}")
 
    def _get_or_404(self, analysis_id: int) -> ImageAnalysis:
        record = self.db.get(ImageAnalysis, analysis_id)
        if record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Image analysis {analysis_id} not found.",
            )
        return record
 
    @staticmethod
    def _to_response(record: ImageAnalysis) -> ImageResponse:
        return ImageResponse(
            success=True,
            message="OK",
            data=ImageData(
                filename=record.filename,
                width=record.width,
                height=record.height,
                image_format=record.image_format,
                file_size=record.file_size,
            ),
        )
 
 
__all__ = ("ImageService",)