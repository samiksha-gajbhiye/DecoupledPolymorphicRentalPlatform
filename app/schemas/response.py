# Response schemas
from typing import Annotated, Any
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.common import BaseResponse
# Base Configuration
MODEL_CONFIG = ConfigDict(
    extra="forbid",
    validate_assignment=True,
)
# Health Response Data
class HealthData(BaseModel):
    """
    Represents the operational health status of the AI service.
    """
    model_config = MODEL_CONFIG
    status: Annotated[
        str,
        Field(
            description="Current operational status of the application.",
            examples=["healthy"],
        ),
    ]
# Version Response Data
class VersionData(BaseModel):
    """
    Represents version information for the deployed AI service.
    """
    model_config = MODEL_CONFIG
    version: Annotated[
        str,
        Field(
            description="Semantic version of the deployed service.",
            examples=["1.0.0"],
        ),
    ]
# Image Processing Response Data
class ImageData(BaseModel):
    """
    Represents metadata extracted from a processed image.
    """
    model_config = MODEL_CONFIG
    filename: Annotated[
        str,
        Field(
            description="Original image filename.",
            examples=["chair.jpg"],
        ),
    ]
    width: Annotated[
        int,
        Field(
            gt=0,
            description="Image width in pixels.",
            examples=[1024],
        ),
    ]
    height: Annotated[
        int,
        Field(
            gt=0,
            description="Image height in pixels.",
            examples=[768],
        ),
    ]
    image_format: Annotated[
        str,
        Field(
            description="Detected image format.",
            examples=["JPEG"],
        ),
    ]
    file_size: Annotated[
        int,
        Field(
            gt=0,
            description="Image size in bytes.",
            examples=[524120],
        ),
    ]
# Search Response Data
class SearchData(BaseModel):
    #Represents the results returned from a marketplace search.
    model_config = MODEL_CONFIG
    results: Annotated[
        list[dict[str, Any]],
        Field(
            default_factory=list,
            description="Collection of matching search results.",
        ),
    ]
# Recommendation Response Data
class RecommendationData(BaseModel):
    #Represents recommendation engine output.
    model_config = MODEL_CONFIG
    recommendations: Annotated[
        list[dict[str, Any]],
        Field(
            default_factory=list,
            description="Recommended rental items for the user.",
        ),
    ]
# Fraud Detection Response Data
class FraudData(BaseModel):
    #Represents fraud detection analysis.
    model_config = MODEL_CONFIG
    risk_score: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="Fraud risk score ranging from 0.0 (safe) to 1.0 (high risk).",
            examples=[0.15],
        ),
    ]
    risk_level: Annotated[
        str,
        Field(
            description="Categorical interpretation of the calculated risk score.",
            examples=["LOW"],
        ),
    ]
# Response Wrappers
class HealthResponse(BaseResponse[HealthData]):

    #Standard response returned by the health check endpoint.
    model_config = MODEL_CONFIG
class VersionResponse(BaseResponse[VersionData]):
    """
    Standard response returned by the version endpoint.
    """
    model_config = MODEL_CONFIG
class ImageResponse(BaseResponse[ImageData]):
    """
    Standard response returned after successful image processing.
    """
    model_config = MODEL_CONFIG
class SearchResponse(BaseResponse[SearchData]):
    """
    Standard response returned by search endpoints.
    """
    model_config = MODEL_CONFIG
class RecommendationResponse(BaseResponse[RecommendationData]):
    """
    Standard response returned by the recommendation engine.
    """
    model_config = MODEL_CONFIG
class FraudResponse(BaseResponse[FraudData]):
    """
    Standard response returned by the fraud detection module.
    """
    model_config = MODEL_CONFIG