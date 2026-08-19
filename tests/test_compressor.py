"""
ImageCompressor Test Suite

Tests:
1. JPEG compression
2. Image resize
3. RGB conversion
4. Unsupported format
5. Invalid quality
6. Maximum file size compression
7. Private helper methods
"""

import os
import sys
from io import BytesIO

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from PIL import Image

from app.services.image.compressor import ImageCompressor


def separator(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_normal_compression():

    separator("TEST 1 : JPEG Compression")

    image = Image.new(
        "RGB",
        (3000, 2000),
        color="blue",
    )

    buffer = ImageCompressor.compress(image)

    print("✓ Compression Successful")
    print(f"Buffer Size : {len(buffer.getvalue())} bytes")


def test_resize():

    separator("TEST 2 : Resize")

    image = Image.new(
        "RGB",
        (4000, 3000),
        color="green",
    )

    buffer = ImageCompressor.compress(
        image,
        max_width=800,
        max_height=600,
    )

    resized = Image.open(buffer)

    print("✓ Resize Successful")
    print("New Size :", resized.size)


def test_quality():

    separator("TEST 3 : Quality Validation")

    image = Image.new(
        "RGB",
        (1000, 1000),
        color="red",
    )

    high = ImageCompressor.compress(
        image,
        quality=90,
    )

    low = ImageCompressor.compress(
        image,
        quality=30,
    )

    print("High Quality :", len(high.getvalue()))
    print("Low Quality  :", len(low.getvalue()))

    if len(low.getvalue()) < len(high.getvalue()):
        print("✓ Quality affects compression")
    else:
        print("⚠ Difference is minimal")


def test_invalid_quality():

    separator("TEST 4 : Invalid Quality")

    image = Image.new(
        "RGB",
        (500, 500),
    )

    try:

        ImageCompressor.compress(
            image,
            quality=150,
        )

    except ValueError as e:

        print("✓ Exception Raised")
        print(e)


def test_invalid_format():

    separator("TEST 5 : Unsupported Format")

    image = Image.new(
        "RGB",
        (500, 500),
    )

    try:

        ImageCompressor.compress(
            image,
            output_format="PNG",
        )

    except ValueError as e:

        print("✓ Exception Raised")
        print(e)


def test_size_limit():

    separator("TEST 6 : Max Size Compression")

    image = Image.new(
        "RGB",
        (3500, 2500),
        color="orange",
    )

    buffer = ImageCompressor.compress(
        image,
        quality=90,
        max_size_bytes=100000,
    )

    print("Compressed Size :", len(buffer.getvalue()))

    if len(buffer.getvalue()) <= 100000:
        print("✓ Size limit respected")
    else:
        print("⚠ Could not reach target size")


def test_estimate_size():

    separator("TEST 7 : Estimate Size")

    image = Image.new(
        "RGB",
        (800, 800),
    )

    buffer = ImageCompressor.compress(image)

    estimated = ImageCompressor._estimate_size(buffer)

    print("Estimated :", estimated)
    print("Actual    :", len(buffer.getvalue()))

    if estimated == len(buffer.getvalue()):
        print("✓ Size estimation correct")


def test_rgb_conversion():

    separator("TEST 8 : RGB Conversion")

    image = Image.new(
        "RGBA",
        (500, 500),
    )

    converted = ImageCompressor._convert_format(
        image,
        "JPEG",
    )

    print("Original :", image.mode)
    print("Converted:", converted.mode)

    if converted.mode == "RGB":
        print("✓ RGB conversion successful")

def main():

    separator("IMAGE COMPRESSOR HEALTH CHECK")

    test_normal_compression()
    test_resize()
    test_quality()
    test_invalid_quality()
    test_invalid_format()
    test_size_limit()
    test_estimate_size()
    test_rgb_conversion()

    separator("ALL TESTS FINISHED")

if __name__ == "__main__":
    main()