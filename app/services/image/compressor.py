from __future__ import annotations

import io

from PIL import Image

from app.utils.image_utils import (
    convert_to_rgb,
    resize_image,
)

SUPPORTED_FORMATS = {
    "JPEG",
    "JPG",
}


class ImageCompressor:
    """Service responsible for resizing and compressing images."""

    @staticmethod
    def compress(
        image: Image.Image,
        *,
        max_width: int = 1920,
        max_height: int = 1080,
        quality: int = 80,
        output_format: str = "JPEG",
        max_size_bytes: int | None = None,
        min_quality: int = 30,
    ) -> io.BytesIO:

        quality = ImageCompressor._validate_quality(quality)
        output_format = output_format.upper()

        if output_format not in SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported output format '{output_format}'. "
                f"Supported formats: {sorted(SUPPORTED_FORMATS)}"
            )

        image = ImageCompressor._convert_format(
            image=image,
            output_format=output_format,
        )

        image = ImageCompressor._resize(
            image=image,
            max_width=max_width,
            max_height=max_height,
        )

        buffer = ImageCompressor._optimize(
            image=image,
            output_format=output_format,
            quality=quality,
        )

        if max_size_bytes is not None:

            current_quality = quality

            for _ in range(6):

                if (
                    ImageCompressor._estimate_size(buffer)
                    <= max_size_bytes
                ):
                    break

                current_quality = max(
                    min_quality,
                    current_quality - 10,
                )

                buffer = ImageCompressor._optimize(
                    image=image,
                    output_format=output_format,
                    quality=current_quality,
                )

        return buffer

    @staticmethod
    def _resize(
        image: Image.Image,
        max_width: int,
        max_height: int,
    ) -> Image.Image:

        return resize_image(
            image=image,
            max_width=max_width,
            max_height=max_height,
        )

    @staticmethod
    def _convert_format(
        image: Image.Image,
        output_format: str,
    ) -> Image.Image:

        if output_format == "JPEG":
            return convert_to_rgb(image)

        return image.copy()

    @staticmethod
    def _optimize(
        image: Image.Image,
        output_format: str,
        quality: int,
    ) -> io.BytesIO:

        buffer = io.BytesIO()

        save_kwargs = {
            "format": output_format,
            "optimize": True,
        }

        if output_format == "JPEG":
            save_kwargs["quality"] = quality

        try:

            image.save(
                buffer,
                **save_kwargs,
            )

            buffer.seek(0)

            return buffer

        except (OSError, ValueError) as exc:
            raise RuntimeError(
                f"Failed to compress image: {exc}"
            ) from exc

    @staticmethod
    def _estimate_size(
        buffer: io.BytesIO,
    ) -> int:

        current_position = buffer.tell()

        buffer.seek(0, io.SEEK_END)

        size = buffer.tell()

        buffer.seek(current_position)

        return size

    @staticmethod
    def _validate_quality(
        quality: int,
    ) -> int:

        if (
            not isinstance(quality, int)
            or isinstance(quality, bool)
            or not (1 <= quality <= 100)
        ):
            raise ValueError(
                "Image quality must be an integer between 1 and 100."
            )

        return quality


__all__ = (
    "ImageCompressor",
)