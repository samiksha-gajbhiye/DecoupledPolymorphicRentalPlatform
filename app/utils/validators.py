# Validators
from pathlib import Path
import re

from app.config.settings import settings

# Module Constants
ALLOWED_IMAGE_EXTENSIONS: set[str] = {
    ".jpg",
    ".jpeg",
}

# Mapping non-standard MIME types to standard MIME types
ALLOWED_MIME_TYPES: set[str] = {
    "image/jpeg",
    "image/jpg",
}

MIN_QUERY_LENGTH = 2
MAX_QUERY_LENGTH = 200
MIN_PAGE_NUMBER = 1
MIN_PAGE_SIZE = 1
MAX_PAGE_SIZE = 100

# Only letters, numbers, spaces, dots, underscores and hyphens
FILENAME_PATTERN = re.compile(r"^[A-Za-z0-9._ -]+$")

# Filename Validation

def validate_filename(filename: str) -> str:
    """Validate and sanitize an uploaded filename."""
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string.")
    
    filename = Path(filename).name.strip()
    if not filename:
        raise ValueError("Filename cannot be empty.")
    
    path_obj = Path(filename)
    # Catch hidden files without a stem (e.g., '.jpg') or invalid path navigation
    if filename in {".", ".."} or not path_obj.stem or not path_obj.suffix:
        raise ValueError("Filename must contain a valid name and extension.")
        
    if not FILENAME_PATTERN.fullmatch(filename):
        raise ValueError("Filename contains invalid characters.")
        
    return filename

# Image Extension Validation

def validate_image_extension(filename: str) -> str:
    """Validate whether the uploaded file has a supported JPEG image extension."""
    filename = validate_filename(filename)
    extension = Path(filename).suffix.lower()
    
    if extension not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValueError(
            f"Unsupported image format '{extension}'. "
            f"Allowed formats: {sorted(ALLOWED_IMAGE_EXTENSIONS)}"
        )
    return filename

# MIME Type Validation

def validate_mime_type(content_type: str) -> str:
    """Validate and normalize the MIME type of an uploaded image."""
    if not isinstance(content_type, str):
        raise ValueError("MIME type must be a string.")
        
    content_type = content_type.strip().lower()
    if content_type not in ALLOWED_MIME_TYPES:
        raise ValueError(f"Unsupported MIME type '{content_type}'.")
        
    # Always normalize non-standard image/jpg to official image/jpeg
    if content_type == "image/jpg":
        return "image/jpeg"
        
    return content_type

# File Size Validation

def validate_file_size(size_in_bytes: int) -> int:
    """Validate uploaded file size."""
    if isinstance(size_in_bytes, bool):
        raise ValueError("File size cannot be boolean.")
    if not isinstance(size_in_bytes, int):
        raise ValueError("File size must be an integer.")
    if size_in_bytes <= 0:
        raise ValueError("File size must be greater than zero.")
        
    max_size = settings.upload.max_image_size
    if size_in_bytes > max_size:
        raise ValueError(
            f"Maximum allowed file size is {max_size} bytes."
        )
    return size_in_bytes

# Search Query Validation

def validate_search_query(query: str) -> str:
    """Normalize and validate a search query."""
    if not isinstance(query, str):
        raise ValueError("Search query must be a string.")
    
    query = re.sub(r"\s+", " ", query).strip()
    if not query:
        raise ValueError("Search query cannot be empty.")
    if len(query) < MIN_QUERY_LENGTH:
        raise ValueError(
            f"Search query must contain at least {MIN_QUERY_LENGTH} characters."
        )
    if len(query) > MAX_QUERY_LENGTH:
        raise ValueError(
            f"Search query cannot exceed {MAX_QUERY_LENGTH} characters."
        )
    return query

# Pagination Validation

def validate_page_number(page: int) -> int:
    """Validate pagination page number."""
    if isinstance(page, bool):
        raise ValueError("Page number cannot be boolean.")
    if not isinstance(page, int):
        raise ValueError("Page number must be an integer.")
    if page < MIN_PAGE_NUMBER:
        raise ValueError(
            f"Page number must be at least {MIN_PAGE_NUMBER}."
        )
    return page

def validate_page_size(page_size: int) -> int:
    """Validate pagination page size."""
    if isinstance(page_size, bool):
        raise ValueError("Page size cannot be boolean.")
    if not isinstance(page_size, int):
        raise ValueError("Page size must be an integer.")
    if not MIN_PAGE_SIZE <= page_size <= MAX_PAGE_SIZE:
        raise ValueError(
            f"Page size must be between "
            f"{MIN_PAGE_SIZE} and {MAX_PAGE_SIZE}."
        )
    return page_size