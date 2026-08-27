# Request schemas
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
# Base Request
class BaseRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
# Pagination Request
class PaginationRequest(BaseRequest):
    """
    Standard pagination parameters used by all list-based endpoints.
    """
    page: Annotated[
        int,
        Field(
            ge=1,
            description="Current page number.",
            examples=[1],
        ),
    ] = 1
    page_size: Annotated[
        int,
        Field(
            ge=1,
            le=100,
            description="Number of records returned per page.",
            examples=[20],
        ),
    ] = 20
# Search Filter Request
class SearchFilterRequest(PaginationRequest):
    """
    Request model used for marketplace search and filtering.
    This model supports searching across properties, furniture,
    electronics, vehicles and future rental categories.
    """
    query: Annotated[
        str,
        Field(
            min_length=2,
            max_length=200,
            description="Search keywords entered by the user.",
            examples=["study table"],
        ),
    ]
    category: Annotated[
        str | None,
        Field(
            default=None,
            max_length=100,
            description="Primary marketplace category.",
            examples=["Furniture"],
        ),
    ]
    subcategory: Annotated[
        str | None,
        Field(
            default=None,
            max_length=100,
            description="Optional subcategory filter.",
            examples=["Study Table"],
        ),
    ]
    city: Annotated[
        str | None,
        Field(
            default=None,
            max_length=100,
            description="City where the rental item should be available.",
            examples=["Nagpur"],
        ),
    ]
# Image Upload Request
class ImageUploadRequest(BaseRequest):
    """
    Metadata accompanying an uploaded image.
    The actual image file is handled separately by FastAPI's UploadFile.
    """
    filename: Annotated[
        str,
        Field(
            min_length=1,
            max_length=255,
            description="Original filename including extension.",
            examples=["chair.jpg"],
        ),
    ]
    content_type: Annotated[
        str,
        Field(
            min_length=3,
            max_length=100,
            description="Standard MIME type of the uploaded image.",
            examples=["image/jpeg"],
        ),
    ]
    file_size: Annotated[
        int,
        Field(
            gt=0,
            description="Image size in bytes.",
            examples=[584231],
        ),
    ]
    description: Annotated[
        str | None,
        Field(
            default=None,
            max_length=500,
            description="Optional description or caption for the image.",
            examples=["Wooden study chair for students."],
        ),
    ]
# Duplicate Comparison Request
class DuplicateCompareRequest(BaseRequest):
    """
    Identifies two already-uploaded images to compare for visual duplication.
    """
    image_id_a: Annotated[
        int,
        Field(
            gt=0,
            description="Analysis ID of the first image.",
            examples=[1],
        ),
    ]
    image_id_b: Annotated[
        int,
        Field(
            gt=0,
            description="Analysis ID of the second image.",
            examples=[2],
        ),
    ]
# Stateless Hash Comparison Request
class HashCompareRequest(BaseRequest):
    """
    Compares a target perceptual hash against one or more candidate hashes.
    Pure computation — no images or database lookups involved. Java supplies
    every hash it wants checked; this never fetches anything on its own.
    """
    target_hash: Annotated[
        str,
        Field(
            min_length=1,
            description="Perceptual hash (hex string) of the newly uploaded image.",
            examples=["ab94d06b0d3b3574"],
        ),
    ]
    candidate_hashes: Annotated[
        list[str],
        Field(
            min_length=1,
            max_length=500,
            description="Perceptual hashes (hex strings) of existing images to check against.",
            examples=[["ab94d06b0d3b3574", "1c2e3f4a5b6c7d8e"]],
        ),
    ]
# Image Compression Request
class ImageCompressRequest(BaseRequest):
    """
    Optional tuning parameters for compressing an already-uploaded image.
    Defaults match ImageCompressor's own defaults.
    """
    quality: Annotated[
        int,
        Field(
            default=80,
            ge=1,
            le=100,
            description="JPEG quality (1-100). Lower means smaller file, more artifacts.",
            examples=[80],
        ),
    ]
    max_width: Annotated[
        int,
        Field(
            default=1920,
            gt=0,
            description="Maximum output width in pixels. Image is downscaled to fit if larger.",
            examples=[1920],
        ),
    ]
    max_height: Annotated[
        int,
        Field(
            default=1080,
            gt=0,
            description="Maximum output height in pixels. Image is downscaled to fit if larger.",
            examples=[1080],
        ),
    ]