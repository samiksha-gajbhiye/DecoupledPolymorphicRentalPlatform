from __future__ import annotations
import io
import sys
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.services.image.classifier import (
    DEFAULT_CATEGORIES,
    ImageClassifier,
)

def create_test_image() -> Image.Image:
    """Load a local test image file."""
    custom_path = Path("test_images/car.jpg")

    if not custom_path.is_file():
        raise FileNotFoundError(f"Image not found at {custom_path}")

    return Image.open(custom_path)

def test_default_categories() -> None:
    print("\n" + "=" * 60)
    print("TEST 1 : DEFAULT CATEGORIES")
    print("=" * 60)

    print("Categories:")

    for category, labels in DEFAULT_CATEGORIES.items():
        print(f"\n{category}")
        print(f"  Labels : {', '.join(labels)}")

    assert isinstance(DEFAULT_CATEGORIES, dict)
    assert len(DEFAULT_CATEGORIES) > 0

    print("\n✅ Default categories test passed")

def test_classifier_initialization() -> ImageClassifier:
    print("\n" + "=" * 60)
    print("TEST 2 : CLASSIFIER INITIALIZATION")
    print("=" * 60)

    print("Loading OpenCLIP model...")
    print("This may take some time on the first run.\n")

    classifier = ImageClassifier()

    print("Model Name :", classifier.model_name)
    print("Pretrained :", classifier.pretrained)
    print("Device     :", classifier.device)
    print("Categories :", len(classifier.categories))
    print("Labels     :", len(classifier._labels))

    assert classifier._model is not None
    assert classifier._transform is not None
    assert classifier._tokenizer is not None
    assert classifier._text_features is not None

    print("\n✅ Classifier initialized successfully")

    return classifier

def test_text_embeddings(classifier: ImageClassifier) -> None:
    print("\n" + "=" * 60)
    print("TEST 3 : TEXT EMBEDDINGS")
    print("=" * 60)

    print("Total labels :", len(classifier._labels))

    print("\nLabels:")

    for label in classifier._labels:
        print(f"  - {label}")

    assert len(classifier._labels) > 0
    assert len(classifier._label_to_category) > 0
    assert classifier._text_features is not None

    print("\nText embedding shape:")
    print(classifier._text_features.shape)

    assert classifier._text_features.shape[0] == len(
        classifier._labels
    )

    print("\n✅ Text embeddings test passed")

def test_pil_image(classifier: ImageClassifier) -> None:
    print("\n" + "=" * 60)
    print("TEST 4 : PIL IMAGE CLASSIFICATION")
    print("=" * 60)

    image = create_test_image()

    print("Image type   :", type(image).__name__)
    print("Image size   :", image.size)
    print("Image mode   :", image.mode)

    result = classifier.classify(image)

    print("\nClassification Result:")
    print(result)

    assert isinstance(result, dict)

    assert "label" in result
    assert "category" in result
    assert "confidence" in result
    assert "predictions" in result
    assert "model" in result
    assert "device" in result

    print("\nPredicted Label :", result["label"])
    print("Category        :", result["category"])
    print("Confidence      :", result["confidence"])
    print("Model           :", result["model"])
    print("Device          :", result["device"])

    print("\nPredictions:")

    for prediction in result["predictions"]:
        print(
            f"  {prediction['label']:<20}"
            f" | {prediction['category']:<15}"
            f" | {prediction['confidence']}"
        )

    print("\n✅ PIL image classification passed")

def test_bytes_input(classifier: ImageClassifier) -> None:
    print("\n" + "=" * 60)
    print("TEST 5 : BYTES INPUT")
    print("=" * 60)

    image = create_test_image()

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="JPEG",
    )

    image_bytes = buffer.getvalue()

    print("Generated JPEG bytes :", len(image_bytes), "bytes")

    result = classifier.classify(image_bytes)

    print("\nClassification Result:")
    print(result)

    assert isinstance(result, dict)
    assert "label" in result
    assert "category" in result
    assert "confidence" in result

    print("\nPredicted Label :", result["label"])
    print("Category        :", result["category"])
    print("Confidence      :", result["confidence"])

    print("\n✅ Bytes input classification passed")

def test_bytesio_input(classifier: ImageClassifier) -> None:
    print("\n" + "=" * 60)
    print("TEST 6 : BYTESIO INPUT")
    print("=" * 60)

    image = create_test_image()

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="PNG",
    )

    buffer.seek(0)

    print("BytesIO buffer created")

    result = classifier.classify(buffer)

    print("\nClassification Result:")
    print(result)

    assert isinstance(result, dict)
    assert "label" in result
    assert "category" in result
    assert "confidence" in result

    print("\nPredicted Label :", result["label"])
    print("Category        :", result["category"])
    print("Confidence      :", result["confidence"])

    print("\n✅ BytesIO input classification passed")

def test_top_k(classifier: ImageClassifier) -> None:
    print("\n" + "=" * 60)
    print("TEST 7 : TOP-K PREDICTIONS")
    print("=" * 60)

    image = create_test_image()

    top_k = 3

    result = classifier.classify(
        image,
        top_k=top_k,
    )

    predictions = result["predictions"]

    print("Requested top_k :", top_k)
    print("Returned       :", len(predictions))
    for index, prediction in enumerate(
        predictions,
        start=1,
    ):
        print(
            f"{index}. "
            f"{prediction['label']} | "
            f"{prediction['category']} | "
            f"{prediction['confidence']}"
        )
    assert len(predictions) == top_k
    print("\n✅ Top-K test passed")
def test_batch_classification(
    classifier: ImageClassifier,
) -> None:
    print("\n" + "=" * 60)
    print("TEST 8 : BATCH CLASSIFICATION")
    print("=" * 60)
    images = [
        create_test_image(),
        create_test_image(),
        create_test_image(),
    ]
    print("Images in batch :", len(images))
    results = classifier.classify_batch(
        images,
        top_k=3,
    )
    print("Results returned:", len(results))
    assert isinstance(results, list)
    assert len(results) == len(images)
    for index, result in enumerate(
        results,
        start=1,
    ):
        print(
            f"\nImage {index}"
        )
        print("  Label      :", result["label"])
        print("  Category   :", result["category"])
        print("  Confidence :", result["confidence"])
        assert isinstance(result, dict)
        assert "label" in result
        assert "category" in result
        assert "confidence" in result

    print("\n✅ Batch classification passed")
def test_invalid_image(classifier: ImageClassifier) -> None:
    print("\n" + "=" * 60)
    print("TEST 9 : INVALID IMAGE INPUT")
    print("=" * 60)

    invalid_input = 12345

    try:
        classifier.classify(invalid_input)
    except TypeError as exc:
        print("Expected TypeError received:")
        print(exc)
        print("\n✅ Invalid image test passed")
        return
    raise AssertionError(
        "Classifier accepted invalid image input."
    )

def test_custom_categories() -> None:
    print("\n" + "=" * 60)
    print("TEST 10 : CUSTOM CATEGORIES")
    print("=" * 60)
    custom_categories = {
        "Furniture": [
            "chair",
            "sofa",
        ],
        "Electronics": [
            "laptop",
            "television",
        ],
    }
    classifier = ImageClassifier(
        categories=custom_categories,
    )

    print("Custom categories:")
    for category, labels in classifier.categories.items():
        print(f"  {category}: {labels}")
    assert classifier.categories == custom_categories
    assert set(classifier._labels) == {
        "chair",
        "sofa",
        "laptop",
        "television",
    }
    print("\n✅ Custom categories test passed")

def main() -> None:

    print("\n")
    print("=" * 60)
    print("IMAGE CLASSIFIER HEALTH CHECK")
    print("=" * 60)

    try:
        classifier = test_classifier_initialization()
        test_text_embeddings(classifier)
        test_pil_image(classifier)
        test_bytes_input(classifier)
        test_bytesio_input(classifier)
        test_top_k(classifier)
        test_batch_classification(classifier)
        test_invalid_image(classifier)
        test_custom_categories()

        print("\n")
        print("=" * 60)
        print("CLASSIFIER STATUS : HEALTHY")
        print("=" * 60)

    except Exception as exc:
        print("\n")
        print("=" * 60)
        print("CLASSIFIER STATUS : FAILED")
        print("=" * 60)

        print(type(exc).__name__)
        print(exc)

        raise
if __name__ == "__main__":
    main()