# Blur detection service
from __future__ import annotations

from io import BytesIO
from typing import Any
import cv2
import numpy as np
from PIL import Image
from app.config.logger import logger
from app.config.settings import settings
from app.utils.image_utils import convert_to_rgb

class BlurDetector:
    """Detect image blur using Laplacian variance."""
    def __init__(
        self,
        threshold: float | None = None,
        normalize_edge: int | None = None,
    ) -> None:
        """Initialize the blur detector.
        Args:
            threshold:
                Minimum Laplacian variance considered sharp.
                Uses settings.ai.blur_threshold when omitted.
            normalize_edge:
                Longest edge, in pixels, that an image is downscaled to
                before being measured.
                Uses settings.ai.blur_normalize_edge when omitted.
        """
        if threshold is not None and threshold < 0:
            raise ValueError(
                "Blur threshold cannot be negative."
            )
        if normalize_edge is not None and normalize_edge < 1:
            raise ValueError(
                "Blur normalize edge must be at least 1 pixel."
            )
        self.threshold = (
            threshold
            if threshold is not None
            else settings.ai.blur_threshold
        )
        self.normalize_edge = (
            normalize_edge
            if normalize_edge is not None
            else settings.ai.blur_normalize_edge
        )
        logger.info(
            f"BlurDetector initialized with threshold={self.threshold:.2f}, "
            f"normalize_edge={self.normalize_edge}"
        )
    def detect(
        self,
        image: Image.Image | bytes | BytesIO,
    ) -> dict[str, Any]:
        """Determine whether an image is blurry."""
        validated_image = self._validate_image(image)
        blur_score = self._calculate_blur_score(
            validated_image
        )
        result = self._postprocess(
            blur_score
        )
        logger.debug(
            f"Blur detection completed: score={result['blur_score']:.2f}, "
            f"blurry={result['is_blurry']}, threshold={self.threshold:.2f}, "
            f"source={validated_image.width}x{validated_image.height}"
        )
        return result
    def _validate_image(
        self,
        image: Image.Image | bytes | BytesIO,
    ) -> Image.Image:
        """Validate and convert input into an RGB PIL image."""
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
    def _normalize_scale(
        self,
        image: Image.Image,
    ) -> Image.Image:
        """Downscale oversized images so scores are comparable across uploads.

        Laplacian variance is resolution-dependent: the same scene measured
        at two different pixel sizes yields two different scores, so a fixed
        threshold only means something if every image is measured at a
        comparable scale. Capping the longest edge does that, and also keeps
        the cost of the Laplacian bounded — a 12MP upload would otherwise be
        ~90x more float64 work on a request path that blocks a product going
        live.
        Downscales only, never upscales. Enlarging a small image interpolates
        new pixels and destroys the edge energy being measured: on this
        project's test images, upscaling to a fixed edge dropped a sharp
        206x244 photo from 1097 to 91 — below several genuinely blurred
        images. Images already within the cap are measured as-is.
        """
        longest_edge = max(image.size)
        if longest_edge <= self.normalize_edge:
            return image
        scale = self.normalize_edge / longest_edge
        return image.resize(
            (
                max(1, round(image.width * scale)),
                max(1, round(image.height * scale)),
            ),
            Image.LANCZOS,
        )
    def _calculate_blur_score(
        self,
        image: Image.Image,
    ) -> float:
        """Calculate the Laplacian variance of an image."""
        measured_image = self._normalize_scale(image)
        image_array = np.asarray(measured_image)
        gray = cv2.cvtColor(
            image_array,
            cv2.COLOR_RGB2GRAY,
        )
        laplacian = cv2.Laplacian(
            gray,
            cv2.CV_64F,
        )
        return float(
            laplacian.var()
        )
    def _postprocess(
        self,
        blur_score: float,
    ) -> dict[str, Any]:
        """Convert the raw score into a structured result."""
        is_blurry = (
            blur_score < self.threshold
        )
        return {
            "blur_score": round(
                blur_score,
                2,
            ),
            "is_blurry": is_blurry,
            "threshold": self.threshold,
        }
__all__ = ("BlurDetector",)