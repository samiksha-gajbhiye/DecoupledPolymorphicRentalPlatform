# Image processing API endpoints
#
# Every endpoint here is stateless: bytes or primitives in, JSON out.
# Nothing is written to disk or to a database — Java owns all storage,
# so there are no analysis IDs and no follow-up lookups.
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from app.config.logger import logger
from app.schemas.common import BaseResponse
from app.schemas.request import HashCompareRequest
from app.schemas.response import (
    CompressionResponse,
    HashCompareResponse,
    HashResponse,
    VerifyResponse,
)
from app.services.image.compression_service import ImageCompressionService
from app.services.image.hash_service import ImageHashService
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
    "/compress",
    response_model=CompressionResponse,
    status_code=status.HTTP_200_OK,
    summary="Compress an image (stateless)",
    description=(
        "Resizes and compresses an uploaded image to JPEG and returns it base64-encoded "
        "alongside the size statistics. Nothing is stored — Java decides where, or "
        "whether, to save the returned bytes."
    ),
)
async def compress_image(
    file: UploadFile = File(...),
    # Sent as multipart form fields, since the image travels in the same request.
    quality: int = Form(default=80, ge=1, le=100, description="JPEG quality, 1-100."),
    max_width: int = Form(default=1920, gt=0, description="Maximum output width in pixels."),
    max_height: int = Form(default=1080, gt=0, description="Maximum output height in pixels."),
) -> CompressionResponse:
    logger.info(f"Compressing image: {file.filename} (quality={quality})")
    try:
        service = ImageCompressionService()
        return await service.compress(
            file,
            quality=quality,
            max_width=max_width,
            max_height=max_height,
        )
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected error occurred while compressing image.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to compress image.",
        ) from exc


@router.get(
    "/health",
    response_model=BaseResponse[dict],
    status_code=status.HTTP_200_OK,
    summary="Image service health",
    description=(
        "Returns the operational status of the image processing service. "
        "Java polls this to decide whether product verification can go ahead."
    ),
)
async def health_check() -> BaseResponse[dict]:
    logger.info("Running image processing health check.")
    try:
        return BaseResponse(
            success=True,
            message="Image Processing Service is healthy.",
            data={"service": "online", "stateless": True},
        )
    except Exception as exc:
        logger.exception("Health check failed.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Health check failed.",
        ) from exc


__all__ = ("router",)
