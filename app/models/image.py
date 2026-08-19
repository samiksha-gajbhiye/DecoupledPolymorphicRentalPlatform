# Image processing models
from __future__ import annotations

import enum
from datetime import datetime
from sqlalchemy import BigInteger, DateTime, Enum, Float, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import Base

class ProcessingStatus(str, enum.Enum):
    """Lifecycle state of the AI image processing pipeline."""
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ImageAnalysis(Base):
    """Stores AI-generated metadata for product images.

    Java owns the Product and ProductImage tables. Python stores only AI-derived 
    information and references Java entities through product_id and image_url.
    """
    __tablename__ = "image_analysis"
    __table_args__ = (
        {"comment": "Stores AI generated metadata, quality metrics and processing state for product images."},
    )

    # Identity
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    image_url: Mapped[str] = mapped_column(String(1024), nullable=False)

    # Image Information
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    width: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    image_format: Mapped[str] = mapped_column(String(20), nullable=False)
    file_size: Mapped[int] = mapped_column(BigInteger, nullable=False)

    # AI Results
    image_hash: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    blur_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    duplicate_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Processing
    processing_status: Mapped[ProcessingStatus] = mapped_column(
        Enum(ProcessingStatus, name="processing_status_enum"),
        nullable=False,
        default=ProcessingStatus.PENDING,
        server_default=ProcessingStatus.PENDING.value,
        index=True,
    )
    processing_time: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
        doc="Processing duration in seconds.",
    )
    processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        doc="Failure reason if processing fails.",
    )

    # Audit
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self) -> str:

        status = (
            self.processing_status.value
            if self.processing_status
            else "None"
        )

        return (
            f"<ImageAnalysis("
            f"id={self.id}, "
            f"product_id={self.product_id}, "
            f"filename='{self.filename}', "
            f"status='{status}'"
            f")>"
        )

__all__ = (
    "ImageAnalysis",
    "ProcessingStatus",
)