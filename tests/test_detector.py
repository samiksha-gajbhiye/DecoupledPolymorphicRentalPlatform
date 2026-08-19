from __future__ import annotations

import os
import sys
from io import BytesIO
from pathlib import Path

from PIL import Image


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
# IMPORT APPLICATION CODE
# ============================================================

from app.config.settings import settings
from app.services.image.detector import ImageDetector


# ============================================================
# TEST IMAGE
# ============================================================

# You can provide an actual image when running the test:
#
# python tests/test_detector.py "path/to/image.jpg"
#
# If no image is provided, a simple generated image is used.
# The generated image is only for testing the pipeline.
TEST_IMAGE_PATH = Path("test_images/car.jpg")


# ============================================================
# HELPERS
# ============================================================

def print_header(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def create_test_image() -> Image.Image:
    """
    Create a simple image for pipeline testing.

    This verifies that the detector can accept and process
    a PIL image even if the model detects zero objects.
    """

    return Image.new(
        "RGB",
        (640, 480),
        color="white",
    )


def load_test_image() -> Image.Image:
    """
    Load a real test image if one was supplied.

    Otherwise create a synthetic image.
    """

    if TEST_IMAGE_PATH is not None:

        if not TEST_IMAGE_PATH.is_file():
            raise FileNotFoundError(
                f"Test image not found: {TEST_IMAGE_PATH}"
            )

        print(
            f"Using test image: {TEST_IMAGE_PATH}"
        )

        return Image.open(
            TEST_IMAGE_PATH
        )

    print(
        "No test image supplied."
    )

    print(
        "Using generated 640x480 test image."
    )

    return create_test_image()


# ============================================================
# TEST 1
# ============================================================

def test_configuration() -> None:

    print_header(
        "TEST 1 : AI Configuration"
    )

    required_settings = (
        "yolo_model",
        "yolo_confidence",
        "yolo_iou_threshold",
        "yolo_max_detections",
        "device",
    )

    missing = []

    for setting_name in required_settings:

        if not hasattr(
            settings.ai,
            setting_name,
        ):
            missing.append(setting_name)

    if missing:

        raise AssertionError(
            "Missing AI settings: "
            + ", ".join(missing)
        )

    print(
        "YOLO Model :",
        settings.ai.yolo_model,
    )

    print(
        "Confidence :",
        settings.ai.yolo_confidence,
    )

    print(
        "IoU        :",
        settings.ai.yolo_iou_threshold,
    )

    print(
        "Max Detect :",
        settings.ai.yolo_max_detections,
    )

    print(
        "Device     :",
        settings.ai.device,
    )

    print(
        "✅ AI configuration verified"
    )


# ============================================================
# TEST 2
# ============================================================

def test_model_initialization() -> ImageDetector:

    print_header(
        "TEST 2 : YOLO Model Initialization"
    )

    detector = ImageDetector()

    print(
        "Model Path :",
        detector.model_path,
    )

    print(
        "Device     :",
        detector.device,
    )

    print(
        "Confidence :",
        detector.confidence,
    )

    print(
        "IoU        :",
        detector.iou_threshold,
    )

    print(
        "Max Detect :",
        detector.max_detections,
    )

    if detector._model is None:

        raise AssertionError(
            "YOLO model was not loaded."
        )

    print(
        "✅ YOLO model loaded successfully"
    )

    return detector


# ============================================================
# TEST 3
# ============================================================

def test_detection_with_pil(
    detector: ImageDetector,
    image: Image.Image,
) -> dict:

    print_header(
        "TEST 3 : Detection Using PIL Image"
    )

    result = detector.detect(
        image
    )

    print(
        "Detection Result:"
    )

    print(
        result
    )

    if not isinstance(
        result,
        dict,
    ):
        raise AssertionError(
            "Detection result is not a dictionary."
        )

    if "objects" not in result:

        raise AssertionError(
            "'objects' missing from result."
        )

    if "object_count" not in result:

        raise AssertionError(
            "'object_count' missing from result."
        )

    if not isinstance(
        result["objects"],
        list,
    ):
        raise AssertionError(
            "'objects' must be a list."
        )

    if result["object_count"] != len(
        result["objects"]
    ):
        raise AssertionError(
            "object_count does not match "
            "number of detected objects."
        )

    print(
        f"Objects Detected : "
        f"{result['object_count']}"
    )

    print(
        "✅ PIL image detection passed"
    )

    return result


# ============================================================
# TEST 4
# ============================================================

def test_detection_structure(
    result: dict,
) -> None:

    print_header(
        "TEST 4 : Detection Result Structure"
    )

    for index, obj in enumerate(
        result["objects"],
        start=1,
    ):

        print(
            f"Object {index}:"
        )

        print(
            "  Label      :",
            obj.get("label"),
        )

        print(
            "  Confidence :",
            obj.get("confidence"),
        )

        print(
            "  BBox       :",
            obj.get("bbox"),
        )

        required_keys = (
            "label",
            "confidence",
            "bbox",
        )

        for key in required_keys:

            if key not in obj:

                raise AssertionError(
                    f"Object {index} "
                    f"is missing '{key}'."
                )

        confidence = obj["confidence"]

        if not isinstance(
            confidence,
            (int, float),
        ):
            raise AssertionError(
                "Confidence must be numeric."
            )

        if not 0 <= confidence <= 100:

            raise AssertionError(
                "Confidence must be "
                "between 0 and 100."
            )

        bbox = obj["bbox"]

        if not isinstance(
            bbox,
            list,
        ):
            raise AssertionError(
                "Bounding box must be a list."
            )

        if len(bbox) != 4:

            raise AssertionError(
                "Bounding box must contain "
                "[x1, y1, x2, y2]."
            )

    print(
        "✅ Detection structure verified"
    )


# ============================================================
# TEST 5
# ============================================================

def test_detection_with_bytes(
    detector: ImageDetector,
    image: Image.Image,
) -> None:

    print_header(
        "TEST 5 : Detection Using Bytes"
    )

    buffer = BytesIO()

    image.save(
        buffer,
        format="JPEG",
    )

    image_bytes = buffer.getvalue()

    result = detector.detect(
        image_bytes
    )

    print(
        "Result:",
        result
    )

    if not isinstance(
        result,
        dict,
    ):
        raise AssertionError(
            "Bytes detection did not return a dictionary."
        )

    print(
        "✅ Bytes input detection passed"
    )


# ============================================================
# TEST 6
# ============================================================

def test_detection_with_bytesio(
    detector: ImageDetector,
    image: Image.Image,
) -> None:

    print_header(
        "TEST 6 : Detection Using BytesIO"
    )

    buffer = BytesIO()

    image.save(
        buffer,
        format="JPEG",
    )

    buffer.seek(0)

    result = detector.detect(
        buffer
    )

    print(
        "Result:",
        result
    )

    if not isinstance(
        result,
        dict,
    ):
        raise AssertionError(
            "BytesIO detection did not return a dictionary."
        )

    print(
        "✅ BytesIO input detection passed"
    )


# ============================================================
# TEST 7
# ============================================================

def test_invalid_input(
    detector: ImageDetector,
) -> None:

    print_header(
        "TEST 7 : Invalid Input Handling"
    )

    try:

        detector.detect(
            "this is not an image"
        )

    except TypeError as exc:

        print(
            "Expected error:",
            exc,
        )

        print(
            "✅ Invalid input correctly rejected"
        )

        return

    raise AssertionError(
        "Invalid input was not rejected."
    )


# ============================================================
# MAIN
# ============================================================

def main() -> None:

    print()
    print("=" * 60)
    print(
        "IMAGE DETECTOR HEALTH CHECK"
    )
    print("=" * 60)

    try:

        # ----------------------------------------------------
        # Configuration
        # ----------------------------------------------------

        test_configuration()

        # ----------------------------------------------------
        # Model
        # ----------------------------------------------------

        detector = test_model_initialization()

        # ----------------------------------------------------
        # Image
        # ----------------------------------------------------

        image = load_test_image()

        print()
        print(
            f"Image Size   : {image.size}"
        )

        print(
            f"Image Format : {image.format}"
        )

        # ----------------------------------------------------
        # Detection
        # ----------------------------------------------------

        result = test_detection_with_pil(
            detector,
            image,
        )

        # ----------------------------------------------------
        # Result
        # ----------------------------------------------------

        test_detection_structure(
            result,
        )

        # ----------------------------------------------------
        # Different Input Types
        # ----------------------------------------------------

        test_detection_with_bytes(
            detector,
            image,
        )

        test_detection_with_bytesio(
            detector,
            image,
        )

        # ----------------------------------------------------
        # Error Handling
        # ----------------------------------------------------

        test_invalid_input(
            detector,
        )

        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        print()
        print("=" * 60)
        print(
            "IMAGE DETECTOR STATUS : HEALTHY"
        )
        print("=" * 60)

    except Exception as exc:

        print()
        print("=" * 60)
        print(
            "IMAGE DETECTOR STATUS : FAILED"
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