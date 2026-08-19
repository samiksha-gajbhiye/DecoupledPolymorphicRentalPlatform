from __future__ import annotations
import os
import sys
from io import BytesIO
import cv2
import numpy as np
from PIL import Image
from pathlib import Path
# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# APPLICATION IMPORT
# ============================================================

from app.services.image.blur_detection import BlurDetector


# ============================================================
# HELPERS
# ============================================================
def create_sharp_test_image() -> Image.Image:
    """Load a specific custom image from disk."""
    custom_path = Path("test_image/blur_car.jpg")

    if not custom_path.is_file():
        raise FileNotFoundError(f"Image not found: {custom_path}")

    return Image.open(custom_path).convert("RGB")
def separator(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def create_sharp_test_image() -> Image.Image:
    """
    Create a high-detail synthetic image.

    Sharp edges produce a higher Laplacian variance,
    making this suitable for testing blur detection.
    """

    image = np.zeros(
        (600, 800, 3),
        dtype=np.uint8,
    )

    # Background
    image[:] = (255, 255, 255)

    # Rectangles
    cv2.rectangle(
        image,
        (50, 50),
        (350, 250),
        (0, 0, 0),
        5,
    )

    cv2.rectangle(
        image,
        (450, 100),
        (750, 300),
        (0, 0, 0),
        5,
    )

    # Lines
    cv2.line(
        image,
        (50, 400),
        (750, 400),
        (0, 0, 0),
        5,
    )

    cv2.line(
        image,
        (100, 450),
        (700, 550),
        (0, 0, 0),
        5,
    )

    # Circle
    cv2.circle(
        image,
        (400, 300),
        100,
        (0, 0, 0),
        5,
    )

    # Text-like detail
    for x in range(100, 700, 50):
        cv2.line(
            image,
            (x, 120),
            (x, 200),
            (0, 0, 0),
            2,
        )

    return Image.fromarray(
        cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB,
        )
    )


def create_blurred_test_image(
    image: Image.Image,
) -> Image.Image:
    """
    Create a heavily blurred version of the test image.
    """

    image_array = np.asarray(image)

    blurred = cv2.GaussianBlur(
        image_array,
        (31, 31),
        0,
    )

    return Image.fromarray(
        blurred
    )


# ============================================================
# TEST 1
# ============================================================

def test_initialization() -> BlurDetector:

    separator(
        "TEST 1 : BLUR DETECTOR INITIALIZATION"
    )

    detector = BlurDetector()

    print(
        "Threshold :",
        detector.threshold,
    )

    assert isinstance(
        detector.threshold,
        (int, float),
    )

    assert detector.threshold >= 0

    print(
        "✅ BlurDetector initialized successfully"
    )

    return detector


# ============================================================
# TEST 2
# ============================================================

def test_sharp_image(
    detector: BlurDetector,
) -> dict:

    separator(
        "TEST 2 : SHARP IMAGE DETECTION"
    )

    image = create_sharp_test_image()

    print(
        "Image Size :",
        image.size,
    )

    result = detector.detect(
        image
    )

    print(
        "Result :",
        result,
    )

    assert isinstance(
        result,
        dict,
    )

    assert "blur_score" in result
    assert "is_blurry" in result
    assert "threshold" in result

    assert isinstance(
        result["blur_score"],
        float,
    )

    assert isinstance(
        result["is_blurry"],
        bool,
    )

    assert result["blur_score"] >= 0

    print(
        "Blur Score :",
        result["blur_score"],
    )

    print(
        "Threshold   :",
        result["threshold"],
    )

    print(
        "Is Blurry   :",
        result["is_blurry"],
    )

    return result


# ============================================================
# TEST 3
# ============================================================

def test_blurred_image(
    detector: BlurDetector,
) -> dict:

    separator(
        "TEST 3 : BLURRED IMAGE DETECTION"
    )

    sharp_image = create_sharp_test_image()

    blurred_image = create_blurred_test_image(
        sharp_image
    )

    result = detector.detect(
        blurred_image
    )

    print(
        "Result :",
        result,
    )

    assert isinstance(
        result,
        dict,
    )

    assert "blur_score" in result
    assert "is_blurry" in result
    assert "threshold" in result

    assert result["blur_score"] >= 0

    print(
        "Blur Score :",
        result["blur_score"],
    )

    print(
        "Threshold   :",
        result["threshold"],
    )

    print(
        "Is Blurry   :",
        result["is_blurry"],
    )

    return result


# ============================================================
# TEST 4
# ============================================================

def test_sharp_vs_blurred(
    detector: BlurDetector,
) -> None:

    separator(
        "TEST 4 : SHARP VS BLURRED"
    )

    sharp_image = create_sharp_test_image()

    blurred_image = create_blurred_test_image(
        sharp_image
    )

    sharp_result = detector.detect(
        sharp_image
    )

    blurred_result = detector.detect(
        blurred_image
    )

    sharp_score = sharp_result[
        "blur_score"
    ]

    blurred_score = blurred_result[
        "blur_score"
    ]

    print(
        f"Sharp Image Score   : {sharp_score}"
    )

    print(
        f"Blurred Image Score : {blurred_score}"
    )

    print(
        f"Difference           : "
        f"{sharp_score - blurred_score:.2f}"
    )

    assert sharp_score > blurred_score, (
        "Sharp image should have a higher "
        "Laplacian variance than the blurred image."
    )

    print(
        "✅ Sharp image has higher detail score"
    )


# ============================================================
# TEST 5
# ============================================================

def test_bytes_input(
    detector: BlurDetector,
) -> None:

    separator(
        "TEST 5 : BYTES INPUT"
    )

    image = create_sharp_test_image()

    buffer = BytesIO()

    image.save(
        buffer,
        format="JPEG",
    )

    image_bytes = buffer.getvalue()

    print(
        "Image bytes :",
        len(image_bytes),
    )

    result = detector.detect(
        image_bytes
    )

    print(
        "Result :",
        result,
    )

    assert isinstance(
        result,
        dict,
    )

    assert "blur_score" in result
    assert "is_blurry" in result

    print(
        "✅ Bytes input test passed"
    )


# ============================================================
# TEST 6
# ============================================================

def test_bytesio_input(
    detector: BlurDetector,
) -> None:

    separator(
        "TEST 6 : BYTESIO INPUT"
    )

    image = create_sharp_test_image()

    buffer = BytesIO()

    image.save(
        buffer,
        format="PNG",
    )

    buffer.seek(0)

    result = detector.detect(
        buffer
    )

    print(
        "Result :",
        result,
    )

    assert isinstance(
        result,
        dict,
    )

    assert "blur_score" in result
    assert "is_blurry" in result

    print(
        "✅ BytesIO input test passed"
    )


# ============================================================
# TEST 7
# ============================================================

def test_invalid_input(
    detector: BlurDetector,
) -> None:

    separator(
        "TEST 7 : INVALID INPUT"
    )

    try:

        detector.detect(
            12345
        )

    except TypeError as exc:

        print(
            "Expected error:"
        )

        print(
            exc
        )

        print(
            "✅ Invalid input correctly rejected"
        )

        return

    raise AssertionError(
        "Invalid input was not rejected."
    )


# ============================================================
# TEST 8
# ============================================================

def test_invalid_image_bytes(
    detector: BlurDetector,
) -> None:

    separator(
        "TEST 8 : INVALID IMAGE BYTES"
    )

    invalid_data = b"This is not an image."

    try:

        detector.detect(
            invalid_data
        )

    except ValueError as exc:

        print(
            "Expected error:"
        )

        print(
            exc
        )

        print(
            "✅ Invalid image bytes correctly rejected"
        )

        return

    raise AssertionError(
        "Invalid image bytes were not rejected."
    )


# ============================================================
# TEST 9
# ============================================================

def test_negative_threshold() -> None:

    separator(
        "TEST 9 : NEGATIVE THRESHOLD"
    )

    try:

        BlurDetector(
            threshold=-1
        )

    except ValueError as exc:

        print(
            "Expected error:"
        )

        print(
            exc
        )

        print(
            "✅ Negative threshold correctly rejected"
        )

        return

    raise AssertionError(
        "Negative threshold was accepted."
    )


# ============================================================
# TEST 10
# ============================================================

def test_custom_threshold() -> None:

    separator(
        "TEST 10 : CUSTOM THRESHOLD"
    )

    custom_threshold = 150.0

    detector = BlurDetector(
        threshold=custom_threshold
    )

    print(
        "Configured threshold :",
        detector.threshold,
    )

    assert detector.threshold == custom_threshold

    print(
        "✅ Custom threshold accepted"
    )


# ============================================================
# MAIN
# ============================================================

def main() -> None:
    separator(
        "BLUR DETECTOR HEALTH CHECK"
    )
    try:
        detector = test_initialization()
        test_sharp_image(
            detector
        )
        test_blurred_image(
            detector
        )
        test_sharp_vs_blurred(
            detector
        )
        test_bytes_input(
            detector
        )
        test_bytesio_input(
            detector
        )
        test_invalid_input(
            detector
        )
        test_invalid_image_bytes(
            detector
        )
        test_negative_threshold()
        test_custom_threshold()
        print()
        print("=" * 60)
        print(
            "BLUR DETECTOR STATUS : HEALTHY"
        )
        print("=" * 60)
    except Exception as exc:
        print()
        print("=" * 60)
        print(
            "BLUR DETECTOR STATUS : FAILED"
        )
        print("=" * 60)
        print(
            type(exc).__name__
        )
        print(
            str(exc)
        )
        print("=" * 60)
        raise
if __name__ == "__main__":
    main()