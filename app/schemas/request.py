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