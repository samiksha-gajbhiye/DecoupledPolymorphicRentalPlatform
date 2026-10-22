from __future__ import annotations

import numpy as np

from app.config.logger import logger
from app.config.settings import settings


class TextEmbedder:
    def __init__(self) -> None:
        from sentence_transformers import SentenceTransformer

        cache_dir = settings.ai.sentence_transformer_directory / "cache"
        cache_dir.mkdir(parents=True, exist_ok=True)

        self._model = SentenceTransformer(
            settings.ai.embedding_model,
            cache_folder=str(cache_dir),
            device="cpu",
        )
        logger.info(f"Loaded text embedding model {settings.ai.embedding_model}")

    def encode(self, texts: list[str]) -> np.ndarray:
        return self._model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )


__all__ = ("TextEmbedder",)
