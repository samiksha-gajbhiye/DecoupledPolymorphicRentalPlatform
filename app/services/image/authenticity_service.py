from __future__ import annotations

import torch
from fastapi import HTTPException, UploadFile, status
from transformers import AutoImageProcessor, AutoModelForImageClassification

from app.config.logger import logger
from app.config.settings import settings
from app.schemas.response import AuthenticityData, AuthenticityResponse
from app.utils.image_utils import load_image


class ImageAuthenticityService:
    """One-shot AI-generated-image check. No database, no disk writes.

    Confirmed 2026-09-12: missed a modern AI-generated image entirely
    (0.0 confidence). One signal, not a verdict -- don't gate solely on
    this. Detectors like this lag behind whatever generators can produce.
    """

    _processor = AutoImageProcessor.from_pretrained(
        settings.ai.authenticity_model,
        cache_dir=settings.ai.authenticity_directory,
    )
    _model = AutoModelForImageClassification.from_pretrained(
        settings.ai.authenticity_model,
        cache_dir=settings.ai.authenticity_directory,
    )
    _model.eval()

    _id2label = {k: v.lower() for k, v in _model.config.id2label.items()}
    _label2id = {v: k for k, v in _id2label.items()}

    _ai_index = None
    for _name in ("artificial", "ai", "fake", "synthetic", "generated", "deepfake"):
        if _name in _label2id:
            _ai_index = _label2id[_name]
            break
    if _ai_index is None:
        logger.warning(f"Could not identify AI-label from id2label={_id2label}; defaulting to 0")
        _ai_index = 0

    async def check(self, file: UploadFile) -> AuthenticityResponse:
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
            inputs = self._processor(images=image, return_tensors="pt")
            with torch.no_grad():
                logits = self._model(**inputs).logits
            probs = torch.softmax(logits, dim=1)[0]
            ai_confidence = probs[self._ai_index].item()
            predicted_index = probs.argmax().item()
            raw_label = self._id2label[predicted_index]
        except Exception as exc:
            logger.exception("Authenticity check failed.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Image authenticity check failed.",
            ) from exc

        is_ai_generated = ai_confidence >= settings.ai.ai_generated_threshold

        logger.info(
            f"Authenticity check filename={file.filename} "
            f"raw_label={raw_label} ai_confidence={ai_confidence:.4f}"
        )

        return AuthenticityResponse(
            success=True,
            message="OK",
            data=AuthenticityData(
                is_ai_generated=is_ai_generated,
                ai_generated_confidence=round(ai_confidence, 4),
                raw_label=raw_label,
            ),
        )


__all__ = ("ImageAuthenticityService",)