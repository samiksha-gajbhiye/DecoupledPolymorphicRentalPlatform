from fastapi import APIRouter, HTTPException, status

from app.config.logger import logger
from app.schemas.request import SemanticRankRequest
from app.schemas.response import SemanticRankResponse
from app.services.search.search_service import SemanticSearchService

router = APIRouter(prefix="/search", tags=["Semantic Search"])


@router.post(
    "/rank",
    response_model=SemanticRankResponse,
    status_code=status.HTTP_200_OK,
    summary="Rank caller-supplied items against a query by meaning (stateless)",
)
def rank_items(request: SemanticRankRequest) -> SemanticRankResponse:
    try:
        return SemanticSearchService().rank(request)
    except Exception as exc:
        logger.exception("Semantic ranking failed.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Semantic search failed.",
        ) from exc
