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