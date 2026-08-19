# Image utilities
from __future__ import annotations
import io
from pathlib import Path
import imagehash
from PIL import Image, ImageOps, UnidentifiedImageError

# Pillow internal format driver name is strictly "JPEG"
CANONICAL_JPEG_FORMAT = "JPEG"
SUPPORTED_IMAGE_FORMATS: set[str] = {"JPG", "JPEG"}
SUPPORTED_HASH_TYPES: set[str] = {"phash", "dhash"}

Image.MAX_IMAGE_PIXELS = 178_956_970


def _normalize_format(fmt: str) -> str:
    """Normalize input format string to standard Pillow format driver name."""
    fmt_upper = fmt.upper()
    if fmt_upper not in SUPPORTED_IMAGE_FORMATS:
        raise ValueError(f"Unsupported image format '{fmt}'. Only JPEG/JPG supported.")
    return CANONICAL_JPEG_FORMAT


def load_image(source: str | Path | bytes | io.BytesIO) -> Image.Image:
    """Load and validate a JPEG image from a file path or memory buffer."""
    try:
        if isinstance(source, (str, Path)):
            image = Image.open(Path(source))
        elif isinstance(source, bytes):
            image = Image.open(io.BytesIO(source))
        elif isinstance(source, io.BytesIO):
            source.seek(0)
            image = Image.open(source)
        else:
            raise ValueError("Unsupported image source.")

        # Force Pillow to read pixel data to detect corrupt streams
        image.load()

        # Strict JPEG enforcement
        if image.format not in SUPPORTED_IMAGE_FORMATS:
            raise ValueError(f"Invalid format '{image.format}'. Only JPEG images are allowed.")

        # Apply EXIF orientation so portrait photos aren't sideways
        image = ImageOps.exif_transpose(image)

        return image
    except (OSError, UnidentifiedImageError, ValueError) as exc:
        raise ValueError(f"Unable to load image: {exc}") from exc


def validate_image(
    source: str | Path | bytes | io.BytesIO,
    raise_on_error: bool = False,
) -> bool:
    """Validate whether an image is readable, uncorrupted, and a valid JPEG."""
    try:
        load_image(source)
        return True
    except ValueError:
        if raise_on_error:
            raise
        return False


def convert_to_rgb(image: Image.Image) -> Image.Image:
    """Convert an image to RGB mode, flattening transparency onto a white background."""
    if image.mode == "RGB":
        return image
    if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
        # Create a solid white background for transparent images converted to JPEG
        background = Image.new("RGB", image.size, (255, 255, 255))
        rgba_image = image.convert("RGBA")
        background.paste(rgba_image, mask=rgba_image.split()[-1])
        return background
    return image.convert("RGB")


def _validate_quality(quality: int) -> None:
    if not 1 <= quality <= 150:
        raise ValueError("quality must be between 1 and 150")

def save_image(
    image: Image.Image,
    destination: str | Path,
    image_format: str = "JPEG",
    quality: int = 90,
) -> Path:
    """Save a Pillow image as JPEG."""
    target_format = _normalize_format(image_format)
    _validate_quality(quality)
    destination = Path(destination)

    output = convert_to_rgb(image)
    output.save(
        destination,
        format=target_format,
        quality=quality,
        optimize=True,
    )
    return destination

def resize_image(
    image: Image.Image,
    max_width: int,
    max_height: int,
) -> Image.Image:
    """Resize an image while preserving its aspect ratio."""
    if max_width <= 0 or max_height <= 0:
        raise ValueError("Image dimensions must be greater than zero.")
    resized = image.copy()
    resized.thumbnail(
        (max_width, max_height),
        Image.Resampling.LANCZOS,
    )
    return resized

def compress_image(
    image: Image.Image,
    quality: int = 80,
    image_format: str = "JPEG",
) -> bytes:
    """Compress an image into JPEG byte stream."""
    target_format = _normalize_format(image_format)
    _validate_quality(quality)

    buffer = io.BytesIO()
    output = convert_to_rgb(image)
    output.save(
        buffer,
        format=target_format,
        quality=quality,
        optimize=True,
    )
    return buffer.getvalue()

def get_image_metadata(image: Image.Image) -> dict[str, str | int]:
    """Return basic image metadata."""
    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
        "format": image.format or "JPEG",
    }

def calculate_image_hash(
    image: Image.Image,
    hash_type: str = "phash",
) -> str:
    """Generate a perceptual image hash."""
    hash_type = hash_type.lower()
    if hash_type not in SUPPORTED_HASH_TYPES:
        raise ValueError(f"Unsupported hash type '{hash_type}'.")

    rgb_image = convert_to_rgb(image)
    hash_functions = {
        "phash": imagehash.phash,
        "dhash": imagehash.dhash,
    }
    return str(hash_functions[hash_type](rgb_image))