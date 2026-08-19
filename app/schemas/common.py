from datetime import UTC, datetime
from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, ConfigDict, Field

# Generic Type
T = TypeVar("T")
# Error Detail Schema
class ErrorDetail(BaseModel):
   # Standard error model returned whenever an API request fails.

    model_config = ConfigDict(extra="forbid")
    code: int = Field(
        ...,
        description="HTTP status code.",
        examples=[404],
    )
    type: str = Field(
        ...,
        description="Machine-readable error category.",
        examples=["ValidationError"],
    )
    detail: Optional[str] = Field(
        default=None,
        description="Detailed explanation of the error.",
        examples=["Uploaded image format is not supported."],
    )

# Pagination Metadata
class PaginationMetadata(BaseModel):

   # Metadata describing a paginated API response.

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )
    page: int = Field(
        ...,
        description="Current page number.",
        examples=[1],
    )
    page_size: int = Field(
        ...,
        description="Number of records per page.",
        examples=[20],
    )
    total_items: int = Field(
        ...,
        description="Total number of available records.",
        examples=[250],
    )
    total_pages: int = Field(
        ...,
        description="Total number of available pages.",
        examples=[13],
    )

# Base API Response
class BaseResponse(BaseModel, Generic[T]):

    #Standard API response wrapper.
    #Every successful or failed endpoint should return this structure.
    model_config = ConfigDict(extra="forbid")
    success: bool = Field(
        default=True,
        description="Indicates whether the request was successful.",
        examples=[True],
    )
    message: str = Field(
        ...,
        description="Human-readable response message.",
        examples=["Image processed successfully."],
    )
    data: Optional[T] = Field(
        default=None,
        description="Actual response payload.",
    )
    error: Optional[ErrorDetail] = Field(
        default=None,
        description="Error information when success=False.",
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp when the response was generated (UTC).",
    )

# Paginated Response
class PaginatedResponse(BaseResponse[T]):
#API response wrapper for paginated resources.
    pagination: PaginationMetadata = Field(
        ...,
        description="Pagination information.",
    )