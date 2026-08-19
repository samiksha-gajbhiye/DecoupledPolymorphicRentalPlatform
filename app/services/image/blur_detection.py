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
    def __init__(self, threshold: float | None = None) -> None:
        """Initialize the blur detector.
        Args:
            threshold:
                Minimum Laplacian variance considered sharp.
                Uses settings.ai.blur_threshold when omitted.
        """
        if threshold is not None and threshold < 0:
            raise ValueError(
                "Blur threshold cannot be negative."
            )
        self.threshold = (
            threshold
            if threshold is not None
            else settings.ai.blur_threshold
        )
        logger.info(
            "BlurDetector initialized with threshold %.2f",
            self.threshold,
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
            "Blur detection completed: score=%.2f, blurry=%s",
            result["blur_score"],
            result["is_blurry"],
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
    def _calculate_blur_score(
        self,
        image: Image.Image,
    ) -> float:
        """Calculate the Laplacian variance of an image."""
        image_array = np.asarray(image)
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