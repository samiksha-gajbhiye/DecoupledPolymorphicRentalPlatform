# Image processing API endpoints
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.logger import logger
from app.schemas.common import BaseResponse
from app.schemas.response import ImageResponse
from app.services.image.image_service import ImageService

router = APIRouter(prefix="/image", tags=["Image Processing"])


@router.post(
    "/upload",
    response_model=ImageResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload an image",
    description="Uploads an image and stores its metadata after validation.",
)
async def upload_image(
    file: UploadFile = File(...),
    product_id: int | None = None,
    db: Session = Depends(get_db),
) -> ImageResponse:
    logger.info(f"Received image upload request: {file.filename}")
    try:
        service = ImageService(db)
        response = await service.upload_image(file=file, product_id=product_id)
        logger.info(f"Image uploaded successfully: {file.filename}")
        return response
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while uploading image.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload image.",
        ) from exc


@router.post(
    "/process/{analysis_id}",
    response_model=ImageResponse,
    status_code=status.HTTP_200_OK,
    summary="Process an uploaded image",
    description="Triggers the AI processing pipeline for an uploaded image.",
)
async def process_image(analysis_id: int, db: Session = Depends(get_db)) -> ImageResponse:
    logger.info(f"Processing image analysis ID: {analysis_id}")
    try:
        service = ImageService(db)
        response = await service.process_image(analysis_id=analysis_id)
        logger.info(f"Image processing completed for analysis ID: {analysis_id}")
        return response
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred during image processing.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process image.",
        ) from exc


@router.get(
    "/{analysis_id}",
    response_model=ImageResponse,
    status_code=status.HTTP_200_OK,
    summary="Retrieve image analysis",
    description="Returns the AI analysis details for a processed image.",
)
async def get_analysis(analysis_id: int, db: Session = Depends(get_db)) -> ImageResponse:
    logger.info(f"Fetching image analysis ID: {analysis_id}")
    try:
        service = ImageService(db)
        response = await service.get_analysis(analysis_id=analysis_id)
        logger.info(f"Successfully fetched image analysis ID: {analysis_id}")
        return response
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while retrieving image analysis.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve image analysis.",
        ) from exc


@router.delete(
    "/{analysis_id}",
    response_model=BaseResponse[None],
    status_code=status.HTTP_200_OK,
    summary="Delete image analysis",
    description="Deletes an existing image analysis record.",
)
async def delete_analysis(analysis_id: int, db: Session = Depends(get_db)) -> BaseResponse[None]:
    logger.info(f"Deleting image analysis ID: {analysis_id}")
    try:
        service = ImageService(db)
        await service.delete_analysis(analysis_id=analysis_id)
        logger.info(f"Image analysis deleted successfully: {analysis_id}")
        return BaseResponse(success=True, message="Image analysis deleted successfully.", data=None)
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while deleting image analysis.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete image analysis.",
        ) from exc


@router.get(
    "/health",
    response_model=BaseResponse[dict],
    status_code=status.HTTP_200_OK,
    summary="Image service health",
    description="Returns the operational status of the image processing service.",
)
async def health_check(db: Session = Depends(get_db)) -> BaseResponse[dict]:
    logger.info("Running image processing health check.")
    try:
        database_status = db.bind is not None
        return BaseResponse(
            success=True,
            message="Image Processing Service is healthy.",
            data={"database": database_status, "service": "online"},
        )
    except Exception as exc:
        logger.exception("Health check failed.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Health check failed.",
        ) from exc


__all__ = ("router",)