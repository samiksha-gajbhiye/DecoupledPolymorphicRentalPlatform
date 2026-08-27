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
# Duplicate Comparison Response Data
class DuplicateData(BaseModel):
    """
    Represents the result of comparing two images for visual duplication.
    """
    model_config = MODEL_CONFIG
    distance: Annotated[
        int,
        Field(
            ge=0,
            description="Hamming distance between the two images' perceptual hashes. Lower means more similar.",
            examples=[3],
        ),
    ]
    similarity: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="Normalized similarity score between 0 (completely different) and 1 (identical).",
            examples=[0.953],
        ),
    ]
    is_duplicate: Annotated[
        bool,
        Field(
            description="Whether the two images are considered duplicates based on the configured threshold.",
            examples=[True],
        ),
    ]
    threshold: Annotated[
        int,
        Field(
            description="Maximum Hamming distance allowed for two images to be considered duplicates.",
            examples=[5],
        ),
    ]
# Image Compression Response Data
class CompressionData(BaseModel):
    """
    Represents the result of compressing an already-uploaded image.
    """
    model_config = MODEL_CONFIG
    original_size: Annotated[
        int,
        Field(
            ge=0,
            description="File size in bytes before compression.",
            examples=[482_113],
        ),
    ]
    compressed_size: Annotated[
        int,
        Field(
            ge=0,
            description="File size in bytes after compression.",
            examples=[118_402],
        ),
    ]
    saved_bytes: Annotated[
        int,
        Field(
            ge=0,
            description="Bytes removed by compression (original_size - compressed_size).",
            examples=[363_711],
        ),
    ]
    saved_percentage: Annotated[
        float,
        Field(
            ge=0.0,
            description="Percentage of the original file size saved.",
            examples=[75.44],
        ),
    ]
    width: Annotated[
        int,
        Field(gt=0, description="Output width in pixels.", examples=[1920]),
    ]
    height: Annotated[
        int,
        Field(gt=0, description="Output height in pixels.", examples=[1080]),
    ]
    image_format: Annotated[
        str,
        Field(description="Output image format.", examples=["JPEG"]),
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
class DuplicateResponse(BaseResponse[DuplicateData]):
    """
    Standard response returned by the duplicate image comparison endpoint.
    """
    model_config = MODEL_CONFIG
class CompressionResponse(BaseResponse[CompressionData]):
    """
    Standard response returned by the image compression endpoint.
    """
    model_config = MODEL_CONFIG
# Stateless Image Verification Response Data
class VerifyData(BaseModel):
    """
    Result of a one-shot, stateless verification: classification + blur check.
    Nothing about the image is stored — this is computed fresh per request.
    """
    model_config = MODEL_CONFIG
    label: Annotated[
        str,
        Field(description="Predicted category label for the image.", examples=["Chair"]),
    ]
    category: Annotated[
        str,
        Field(description="Broader category grouping for the predicted label.", examples=["Furniture"]),
    ]
    confidence: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="Model confidence in the predicted label.",
            examples=[0.9123],
        ),
    ]
    is_blurry: Annotated[
        bool,
        Field(description="Whether the image was flagged as too blurry.", examples=[False]),
    ]
    blur_score: Annotated[
        float,
        Field(description="Raw sharpness score. Lower means blurrier.", examples=[184.32]),
    ]
    width: Annotated[int, Field(gt=0, examples=[1920])]
    height: Annotated[int, Field(gt=0, examples=[1080])]
    image_format: Annotated[str, Field(examples=["JPEG"])]
    file_size: Annotated[int, Field(ge=0, examples=[482_113])]
class VerifyResponse(BaseResponse[VerifyData]):
    """
    Standard response returned by the stateless /image/verify endpoint.
    """
    model_config = MODEL_CONFIG
# Stateless Hash Response Data
class HashData(BaseModel):
    """
    Result of computing a perceptual hash for a single image.
    Nothing is stored — Java is responsible for persisting this hash.
    """
    model_config = MODEL_CONFIG
    hash: Annotated[
        str,
        Field(description="Perceptual hash of the image, as a hex string.", examples=["ab94d06b0d3b3574"]),
    ]
    hash_size: Annotated[
        int,
        Field(description="Hash grid size used to compute this hash (must match on both sides of a comparison).", examples=[8]),
    ]
class HashResponse(BaseResponse[HashData]):
    """
    Standard response returned by the /image/hash endpoint.
    """
    model_config = MODEL_CONFIG
# Stateless Hash Comparison Response Data
class HashMatchResult(BaseModel):
    """
    Result of comparing the target hash against a single candidate hash.
    """
    model_config = MODEL_CONFIG
    candidate_hash: Annotated[
        str,
        Field(description="The candidate hash this result corresponds to.", examples=["ab94d06b0d3b3574"]),
    ]
    distance: Annotated[
        int,
        Field(ge=0, description="Hamming distance between the two hashes. Lower means more similar.", examples=[3]),
    ]
    similarity: Annotated[
        float,
        Field(ge=0.0, le=1.0, description="Normalized similarity score between 0 and 1.", examples=[0.953]),
    ]
    is_duplicate: Annotated[
        bool,
        Field(description="Whether this candidate is considered a duplicate of the target.", examples=[True]),
    ]
class HashCompareData(BaseModel):
    """
    Result of comparing one target hash against a batch of candidate hashes.
    """
    model_config = MODEL_CONFIG
    threshold: Annotated[
        int,
        Field(description="Maximum Hamming distance allowed to be considered a duplicate.", examples=[5]),
    ]
    results: Annotated[
        list[HashMatchResult],
        Field(description="One result per candidate hash, in the same order they were supplied."),
    ]
class HashCompareResponse(BaseResponse[HashCompareData]):
    """
    Standard response returned by the /image/compare-hashes endpoint.
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