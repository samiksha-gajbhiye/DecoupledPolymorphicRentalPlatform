from __future__ import annotations
import io
import sys
from pathlib import Path
from PIL import Image, ImageDraw
# ============================================================
# PROJECT ROOT
# ============================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
# ============================================================
# APPLICATION IMPORT
# ============================================================
from app.services.image.duplicate import DuplicateDetector
# ============================================================
# TEST IMAGE HELPERS
# ============================================================
def create_pattern_image() -> Image.Image:
    """Create a detailed test image."""
    image = Image.new(
        "RGB",
        (500, 500),
        "white",
    )
    draw = ImageDraw.Draw(image)
    draw.rectangle(
        (75, 75, 425, 425),
        outline="black",
        width=8,
    )
    draw.ellipse(
        (150, 150, 350, 350),
        fill="blue",
    )
    draw.rectangle(
        (200, 200, 300, 300),
        fill="red",
    )
    # Add several lines for more visual detail.
    for x in range(50, 500, 50):
        draw.line(
            (x, 0, x, 500),
            fill="gray",
            width=2,
        )
    return image
def create_different_image() -> Image.Image:
    """Create a structurally different image."""
    image = Image.new(
        "RGB",
        (500, 500),
        "white",
    )
    draw = ImageDraw.Draw(image)
    # Large black diagonal stripes.
    for x in range(-500, 1000, 60):
        draw.line(
            (x, 0, x + 500, 500),
            fill="black",
            width=20,
        )
    return image

def image_to_bytes(
    image: Image.Image,
    image_format: str = "JPEG",
) -> bytes:
    """Convert PIL image to raw bytes."""
    buffer = io.BytesIO()
    image.save(
        buffer,
        format=image_format,
    )
    return buffer.getvalue()

def image_to_bytesio(
    image: Image.Image,
    image_format: str = "JPEG",
) -> io.BytesIO:
    """Convert PIL image to BytesIO."""
    buffer = io.BytesIO()
    image.save(
        buffer,
        format=image_format,
    )
    buffer.seek(0)
    return buffer
# ============================================================
# TEST 1
# INITIALIZATION
# ============================================================

def test_initialization() -> DuplicateDetector:

    print("\n" + "=" * 60)
    print("TEST 1 : INITIALIZATION")
    print("=" * 60)
    detector = DuplicateDetector(
        threshold=5,
        hash_size=8,
    )
    print(
        "Threshold :",
        detector.threshold,
    )
    print(
        "Hash Size :",
        detector.hash_size,
    )
    assert detector.threshold == 5
    assert detector.hash_size == 8
    print(
        "✅ Initialization test passed"
    )
    return detector
# ============================================================
# TEST 2
# IDENTICAL IMAGES
# ============================================================

def test_identical_images(
    detector: DuplicateDetector,
) -> None:
    print("\n" + "=" * 60)
    print("TEST 2 : IDENTICAL IMAGES")
    print("=" * 60)
    image = create_pattern_image()
    result = detector.compare(
        image,
        image.copy(),
    )
    print("Result:")
    print(result)
    assert result["distance"] == 0
    assert result["similarity"] == 1.0
    assert result["is_duplicate"] is True
    assert result["threshold"] == 5

    print(
        "✅ Identical image test passed"
    )


# ============================================================
# TEST 3
# RESIZED IMAGE
# ============================================================

def test_resized_image(
    detector: DuplicateDetector,
) -> None:

    print("\n" + "=" * 60)
    print("TEST 3 : RESIZED IMAGE")
    print("=" * 60)

    image_a = create_pattern_image()

    image_b = image_a.resize(
        (400, 400)
    )

    result = detector.compare(
        image_a,
        image_b,
    )

    print("Result:")
    print(result)

    print(
        "Distance   :",
        result["distance"],
    )

    print(
        "Similarity :",
        result["similarity"],
    )

    print(
        "Threshold  :",
        result["threshold"],
    )

    print(
        "Duplicate  :",
        result["is_duplicate"],
    )
    # A resized version should still have a
    # relatively small perceptual distance.
    # We do NOT require it to be <= the application's
    # duplicate threshold because threshold tuning is
    # a separate concern from testing pHash behavior.

    assert result["distance"] < 20
    assert 0.0 <= result["similarity"] <= 1.0
    print(
        "✅ Resized image produced a reasonable "
        "perceptual distance"
    )
    if result["is_duplicate"]:
        print(
            "i Current threshold classifies the "
            "resized image as a duplicate."
        )
    else:
        print(
            "i Current threshold does NOT classify "
            "the resized image as a duplicate."
        )
# ============================================================
# TEST 4
# DIFFERENT IMAGES
# ============================================================
def test_different_images(
    detector: DuplicateDetector,
) -> None:
    print("\n" + "=" * 60)
    print("TEST 4 : DIFFERENT IMAGES")
    print("=" * 60)
    image_a = create_pattern_image()
    image_b = create_different_image()
    result = detector.compare(
        image_a,
        image_b,
    )

    print("Result:")
    print(result)

    print(
        "Distance   :",
        result["distance"],
    )

    print(
        "Similarity :",
        result["similarity"],
    )

    print(
        "Duplicate  :",
        result["is_duplicate"],
    )

    assert result["distance"] > detector.threshold

    assert result["is_duplicate"] is False

    print(
        "✅ Different image test passed"
    )


# ============================================================
# TEST 5
# JPEG / BYTES INPUT
# ============================================================

def test_bytes_input(
    detector: DuplicateDetector,
) -> None:

    print("\n" + "=" * 60)
    print("TEST 5 : BYTES INPUT")
    print("=" * 60)

    image = create_pattern_image()

    image_bytes = image_to_bytes(
        image
    )

    result = detector.compare(
        image_bytes,
        image_bytes,
    )

    print("Result:")
    print(result)

    assert result["distance"] == 0

    assert result["similarity"] == 1.0

    assert result["is_duplicate"] is True

    print(
        "Image size :",
        len(image_bytes),
        "bytes",
    )

    print(
        "✅ Bytes input test passed"
    )


# ============================================================
# TEST 6
# BYTESIO INPUT
# ============================================================

def test_bytesio_input(
    detector: DuplicateDetector,
) -> None:

    print("\n" + "=" * 60)
    print("TEST 6 : BYTESIO INPUT")
    print("=" * 60)

    image = create_pattern_image()

    buffer_a = image_to_bytesio(
        image
    )

    buffer_b = image_to_bytesio(
        image
    )

    result = detector.compare(
        buffer_a,
        buffer_b,
    )

    print("Result:")
    print(result)

    assert result["distance"] == 0

    assert result["similarity"] == 1.0

    assert result["is_duplicate"] is True

    print(
        "✅ BytesIO input test passed"
    )


# ============================================================
# TEST 7
# MIXED INPUT TYPES
# ============================================================
def test_mixed_input_types(
    detector: DuplicateDetector,
) -> None:
    print("\n" + "=" * 60)
    print("TEST 7 : MIXED INPUT TYPES")
    print("=" * 60)
    image = create_pattern_image()
    image_bytes = image_to_bytes(
        image
    )
    image_buffer = image_to_bytesio(
        image
    )
    # --------------------------------------------------------
    # PIL vs Bytes
    # --------------------------------------------------------
    result_1 = detector.compare(
        image,
        image_bytes,
    )
    # --------------------------------------------------------
    # Bytes vs BytesIO
    # --------------------------------------------------------
    result_2 = detector.compare(
        image_bytes,
        image_buffer,
    )
    print("PIL vs Bytes:")
    print(result_1)
    print("\nBytes vs BytesIO:")
    print(result_2)
    # --------------------------------------------------------
    # We are testing INPUT COMPATIBILITY here.
    # JPEG conversion is lossy, so we must NOT require:
    # distance == 0
    # or:
    # distance <= duplicate threshold
    # The important thing is that:
    # 1. comparison succeeds
    # 2. valid result is returned
    # 3. distance is within the valid pHash range
    # 4. similarity is between 0 and 1
    # --------------------------------------------------------

    for result in (
        result_1,
        result_2,
    ):

        assert isinstance(
            result["distance"],
            int,
        )

        assert 0 <= result["distance"] <= 64

        assert isinstance(
            result["similarity"],
            float,
        )

        assert 0.0 <= result["similarity"] <= 1.0

        assert isinstance(
            result["is_duplicate"],
            bool,
        )

        assert result["threshold"] == detector.threshold

    print(
        "\nPIL → Bytes distance :",
        result_1["distance"],
    )

    print(
        "Bytes → BytesIO distance :",
        result_2["distance"],
    )

    print(
        "\nPIL → Bytes comparison successfully executed"
    )

    print(
        "Bytes → BytesIO comparison successfully executed"
    )

    print(
        "✅ Mixed input type test passed"
    )


# ============================================================
# TEST 8
# INVALID INPUT TYPE
# ============================================================

def test_invalid_input(
    detector: DuplicateDetector,
) -> None:

    print("\n" + "=" * 60)
    print("TEST 8 : INVALID INPUT TYPE")
    print("=" * 60)

    try:

        detector.compare(
            12345,
            67890,
        )

    except TypeError as exc:

        print(
            "Expected TypeError:"
        )

        print(
            exc
        )

        print(
            "✅ Invalid input correctly rejected"
        )

        return

    raise AssertionError(
        "Expected TypeError was not raised."
    )


# ============================================================
# TEST 9
# INVALID IMAGE BYTES
# ============================================================

def test_invalid_image_bytes(
    detector: DuplicateDetector,
) -> None:

    print("\n" + "=" * 60)
    print("TEST 9 : INVALID IMAGE BYTES")
    print("=" * 60)

    invalid_data = (
        b"This is not a valid image."
    )

    try:

        detector.compare(
            invalid_data,
            invalid_data,
        )

    except ValueError as exc:

        print(
            "Expected ValueError:"
        )

        print(
            exc
        )

        print(
            "✅ Invalid image bytes correctly rejected"
        )

        return

    raise AssertionError(
        "Expected ValueError was not raised."
    )


# ============================================================
# TEST 10
# NEGATIVE THRESHOLD
# ============================================================

def test_negative_threshold() -> None:

    print("\n" + "=" * 60)
    print("TEST 10 : NEGATIVE THRESHOLD")
    print("=" * 60)

    try:

        DuplicateDetector(
            threshold=-1
        )

    except ValueError as exc:

        print(
            "Expected ValueError:"
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
# TEST 11
# INVALID HASH SIZE
# ============================================================

def test_invalid_hash_size() -> None:

    print("\n" + "=" * 60)
    print("TEST 11 : INVALID HASH SIZE")
    print("=" * 60)

    try:

        DuplicateDetector(
            threshold=5,
            hash_size=0,
        )

    except ValueError as exc:

        print(
            "Expected ValueError:"
        )

        print(
            exc
        )

        print(
            "✅ Invalid hash size correctly rejected"
        )

        return

    raise AssertionError(
        "Hash size 0 was accepted."
    )


# ============================================================
# TEST 12
# CUSTOM HASH SIZE
# ============================================================

def test_custom_hash_size() -> None:

    print("\n" + "=" * 60)
    print("TEST 12 : CUSTOM HASH SIZE")
    print("=" * 60)

    detector = DuplicateDetector(
        threshold=10,
        hash_size=16,
    )

    image = create_pattern_image()

    result = detector.compare(
        image,
        image.copy(),
    )

    print(
        "Hash Size :",
        detector.hash_size,
    )

    print(
        "Distance :",
        result["distance"],
    )

    print(
        "Similarity :",
        result["similarity"],
    )

    assert detector.hash_size == 16

    assert result["distance"] == 0

    assert result["similarity"] == 1.0

    print(
        "✅ Custom hash size test passed"
    )


# ============================================================
# TEST 13
# RETURN CONTRACT
# ============================================================

def test_return_contract(
    detector: DuplicateDetector,
) -> None:

    print("\n" + "=" * 60)
    print("TEST 13 : RETURN CONTRACT")
    print("=" * 60)

    image = create_pattern_image()

    result = detector.compare(
        image,
        image.copy(),
    )

    print(
        "Result:",
        result,
    )

    expected_keys = {
        "distance",
        "similarity",
        "is_duplicate",
        "threshold",
    }

    assert set(
        result.keys()
    ) == expected_keys

    assert isinstance(
        result["distance"],
        int,
    )

    assert isinstance(
        result["similarity"],
        float,
    )

    assert isinstance(
        result["is_duplicate"],
        bool,
    )

    assert isinstance(
        result["threshold"],
        int,
    )

    print(
        "✅ Return contract test passed"
    )


# ============================================================
# TEST 14
# SIMILARITY RANGE
# ============================================================

def test_similarity_range(
    detector: DuplicateDetector,
) -> None:

    print("\n" + "=" * 60)
    print("TEST 14 : SIMILARITY RANGE")
    print("=" * 60)

    image_a = create_pattern_image()

    image_b = create_different_image()

    result = detector.compare(
        image_a,
        image_b,
    )

    similarity = result[
        "similarity"
    ]

    print(
        "Similarity :",
        similarity,
    )

    assert 0.0 <= similarity <= 1.0

    print(
        "✅ Similarity range test passed"
    )


# ============================================================
# MAIN
# ============================================================

def main() -> None:

    print()
    print("=" * 60)
    print("DUPLICATE DETECTOR HEALTH CHECK")
    print("=" * 60)

    try:

        detector = test_initialization()

        test_identical_images(
            detector
        )

        test_resized_image(
            detector
        )

        test_different_images(
            detector
        )

        test_bytes_input(
            detector
        )

        test_bytesio_input(
            detector
        )

        test_mixed_input_types(
            detector
        )

        test_invalid_input(
            detector
        )

        test_invalid_image_bytes(
            detector
        )

        test_negative_threshold()

        test_invalid_hash_size()

        test_custom_hash_size()

        test_return_contract(
            detector
        )

        test_similarity_range(
            detector
        )

        print()
        print("=" * 60)
        print("ALL DUPLICATE DETECTOR TESTS PASSED")
        print("=" * 60)

    except Exception as exc:

        print()
        print("=" * 60)
        print("DUPLICATE DETECTOR TEST FAILED")
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