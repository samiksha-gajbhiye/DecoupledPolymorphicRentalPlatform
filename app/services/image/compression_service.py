from __future__ import annotations

import base64
from io import BytesIO

from fastapi import HTTPException, UploadFile, status
from PIL import Image

from app.config.logger import logger
from app.schemas.response import CompressionData, CompressionResponse
from app.services.image.compressor import ImageCompressor


class ImageCompressionService:
    """Stateless compression. No database, no disk writes.

    The compressed image is returned as base64 inside the JSON response
    rather than as a raw binary body, which keeps it consistent with the
    other stateless endpoints and testable from Postman. Java decides
    where — or whether — to save the result.
    """

    async def compress(
        self,
        file: UploadFile,
        *,
        quality: int = 80,
        max_width: int = 1920,
        max_height: int = 1080,
    ) -> CompressionResponse:
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
            buffer = ImageCompressor.compress(
                image,
                max_width=max_width,
                max_height=max_height,
                quality=quality,
            )
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(exc),
            ) from exc
        except Exception as exc:
            logger.exception("Compression failed.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to compress image.",
            ) from exc

        compressed_bytes = buffer.getvalue()
        original_size = len(raw_bytes)
        compressed_size = len(compressed_bytes)

        # An already-optimized small image can come out slightly larger after
        # re-encoding. Report zero saved rather than a negative number.
        saved_bytes = max(0, original_size - compressed_size)
        saved_percentage = (
            round(saved_bytes / original_size * 100, 2) if original_size else 0.0
        )

        with Image.open(BytesIO(compressed_bytes)) as compressed_image:
            width, height = compressed_image.size
            image_format = (compressed_image.format or "JPEG").upper()

        logger.info(
            f"Compressed image filename={file.filename} "
            f"{original_size}B -> {compressed_size}B ({saved_percentage}% saved) "
            f"{width}x{height} quality={quality}"
        )

        return CompressionResponse(
            success=True,
            message="OK",
            data=CompressionData(
                original_size=original_size,
                compressed_size=compressed_size,
                saved_bytes=saved_bytes,
                saved_percentage=saved_percentage,
                width=width,
                height=height,
                image_format=image_format,
                compressed_image_base64=base64.b64encode(compressed_bytes).decode("ascii"),
            ),
        )


__all__ = ("ImageCompressionService",)
