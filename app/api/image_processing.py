# Image processing API endpoints
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.logger import logger
from app.schemas.common import BaseResponse
from app.schemas.request import DuplicateCompareRequest, HashCompareRequest, ImageCompressRequest
from app.schemas.response import (
    CompressionResponse,
    DuplicateResponse,
    HashCompareResponse,
    HashResponse,
    ImageResponse,
    VerifyResponse,
)
from app.services.image.hash_service import ImageHashService
from app.services.image.image_service import ImageService
from app.services.image.verification_service import ImageVerificationService

router = APIRouter(prefix="/image", tags=["Image Processing"])


@router.post(
    "/verify",
    response_model=VerifyResponse,
    status_code=status.HTTP_200_OK,
    summary="Verify an image (stateless)",
    description=(
        "One-shot classification + blur check for a single image. "
        "Nothing is stored — Java is responsible for persisting the result. "
        "This is the endpoint Java calls at product registration time."
    ),
)
async def verify_image(file: UploadFile = File(...)) -> VerifyResponse:
    logger.info(f"Verifying image: {file.filename}")
    try:
        service = ImageVerificationService()
        response = await service.verify(file)
        return response
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred during image verification.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to verify image.",
        ) from exc


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


@router.post(
    "/compress/{analysis_id}",
    response_model=CompressionResponse,
    status_code=status.HTTP_200_OK,
    summary="Compress an image",
    description="Resizes and compresses an already-uploaded image in place, converting it to JPEG.",
)
async def compress_image(
    analysis_id: int,
    payload: ImageCompressRequest = ImageCompressRequest(),
    db: Session = Depends(get_db),
) -> CompressionResponse:
    logger.info(f"Compressing analysis ID: {analysis_id}")
    try:
        service = ImageService(db)
        response = await service.compress_image(
            analysis_id=analysis_id,
            quality=payload.quality,
            max_width=payload.max_width,
            max_height=payload.max_height,
        )
        return response
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while compressing image.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to compress image.",
        ) from exc


@router.post(
    "/hash",
    response_model=HashResponse,
    status_code=status.HTTP_200_OK,
    summary="Compute an image's perceptual hash (stateless)",
    description=(
        "Computes a perceptual hash for a single image. Nothing is stored — "
        "Java is responsible for persisting the returned hash for later comparisons."
    ),
)
async def compute_image_hash(file: UploadFile = File(...)) -> HashResponse:
    logger.info(f"Computing hash for: {file.filename}")
    try:
        service = ImageHashService()
        return await service.compute_hash(file)
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while computing image hash.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to compute image hash.",
        ) from exc


@router.post(
    "/compare-hashes",
    response_model=HashCompareResponse,
    status_code=status.HTTP_200_OK,
    summary="Compare a hash against candidate hashes (stateless)",
    description=(
        "Pure computation — compares one target perceptual hash against one or more "
        "candidate hashes Java supplies. No images or database lookups involved."
    ),
)
async def compare_image_hashes(payload: HashCompareRequest) -> HashCompareResponse:
    logger.info(f"Comparing target hash against {len(payload.candidate_hashes)} candidate(s)")
    try:
        service = ImageHashService()
        return await service.compare_hashes(
            target_hash=payload.target_hash,
            candidate_hashes=payload.candidate_hashes,
        )
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while comparing image hashes.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to compare image hashes.",
        ) from exc


@router.post(
    "/compare",
    response_model=DuplicateResponse,
    status_code=status.HTTP_200_OK,
    summary="Compare two images for duplication",
    description="Compares two already-uploaded images using perceptual hashing and returns a similarity score.",
)
async def compare_images(
    payload: DuplicateCompareRequest,
    db: Session = Depends(get_db),
) -> DuplicateResponse:
    logger.info(f"Comparing analysis IDs {payload.image_id_a} vs {payload.image_id_b}")
    try:
        service = ImageService(db)
        response = await service.compare_images(
            image_id_a=payload.image_id_a,
            image_id_b=payload.image_id_b,
        )
        return response
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while comparing images.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to compare images.",
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