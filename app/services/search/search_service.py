from __future__ import annotations

from functools import lru_cache

import numpy as np

from app.config.logger import logger
from app.config.settings import settings
from app.schemas.request import SemanticRankRequest
from app.schemas.response import RankedItem, SemanticRankData, SemanticRankResponse
from app.services.search.embeddings import TextEmbedder


@lru_cache(maxsize=1)
def get_embedder() -> TextEmbedder:
    return TextEmbedder()


class SemanticSearchService:
    """Stateless ranking: embed query and items, return ids ordered by similarity."""

    def rank(self, request: SemanticRankRequest) -> SemanticRankResponse:
        texts = [request.query] + [item.text for item in request.items]
        vectors = get_embedder().encode(texts)
        scores = vectors[1:] @ vectors[0]

        results: list[RankedItem] = []
        for index in np.argsort(-scores):
            score = float(scores[index])
            if score < settings.ai.search_min_score:
                break
            results.append(
                RankedItem(
                    id=request.items[index].id,
                    score=round(score, 4),
                    strong=score >= settings.ai.search_strong_score,
                )
            )
            if len(results) >= request.top_k:
                break

        top = ", ".join(f"{r.id}:{r.score}" for r in results[:5])
        logger.info(
            f"Ranked {len(request.items)} items for query={request.query!r} "
            f"returned={len(results)} top=[{top}]"
        )

        return SemanticRankResponse(
            success=True,
            message="OK",
            data=SemanticRankData(query=request.query, results=results),
        )


__all__ = ("SemanticSearchService", "get_embedder")
