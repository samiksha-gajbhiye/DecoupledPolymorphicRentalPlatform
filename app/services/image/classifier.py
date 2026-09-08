from __future__ import annotations

from copy import deepcopy
from io import BytesIO
from typing import Any

import open_clip
import torch
from PIL import Image

from app.config.logger import logger
from app.config.settings import settings
from app.utils.image_utils import convert_to_rgb


DEFAULT_CATEGORIES: dict[str, list[str]] = {
    "Furniture": [
        "chair",
        "table",
        "sofa",
        "bed",
        "desk",
        "bookshelf",
        "wardrobe",
        "cabinet",
    ],
    "Electronics": [
        "laptop",
        "smartphone",
        "television",
        "monitor",
        "camera",
        "headphones",
        "printer",
    ],
    "Appliances": [
        "refrigerator",
        "washing machine",
        "microwave",
        "air conditioner",
        "vacuum cleaner",
    ],
    "Vehicles": [
        "car",
        "motorcycle",
        "bicycle",
        "scooter",
    ],
}


class ImageClassifier:
    """Zero-shot image classifier powered by OpenCLIP."""

    def __init__(
        self,
        model_name: str | None = None,
        pretrained: str | None = None,
        device: str | None = None,
        categories: dict[str, list[str]] | None = None,
    ) -> None:
        self.model_name = model_name or settings.ai.clip_model_name
        self.pretrained = pretrained or settings.ai.clip_pretrained

        requested_device = (device or settings.ai.device).lower()

        if requested_device.startswith("cuda") and not torch.cuda.is_available():
            logger.warning(
                "CUDA requested but unavailable. Falling back to CPU."
            )
            requested_device = "cpu"

        self.device = torch.device(requested_device)

        self.categories = (
            deepcopy(categories)
            if categories is not None
            else deepcopy(DEFAULT_CATEGORIES)
        )

        self._validate_categories()

        self._labels: list[str] = []
        self._label_to_category: dict[str, str] = {}

        self._model: torch.nn.Module | None = None
        self._transform = None
        self._tokenizer = None
        self._text_features: torch.Tensor | None = None

        logger.info(
            f"Initializing OpenCLIP ({self.model_name} - {self.pretrained}) "
            f"on {self.device}"
        )

        self._load_model()
        self._prepare_text_embeddings()
        self._warmup_model()

        logger.info("ImageClassifier initialized successfully.")

    def _validate_categories(self) -> None:
        """Validate category structure."""
        if not isinstance(self.categories, dict):
            raise TypeError("Categories must be a dictionary.")

        if not self.categories:
            raise ValueError("Categories dictionary cannot be empty.")

        for category, labels in self.categories.items():
            if not isinstance(category, str):
                raise TypeError("Category names must be strings.")

            if not isinstance(labels, list):
                raise TypeError(
                    f"Labels for '{category}' must be a list."
                )

            if not labels:
                raise ValueError(
                    f"Category '{category}' contains no labels."
                )

            for label in labels:
                if not isinstance(label, str):
                    raise TypeError(
                        f"Invalid label inside '{category}'."
                    )

    def _load_model(self) -> None:
        """Load the OpenCLIP model and preprocessing pipeline."""
        try:
            model, _, preprocess = open_clip.create_model_and_transforms(
                model_name=self.model_name,
                pretrained=self.pretrained,
            )

            tokenizer = open_clip.get_tokenizer(
                self.model_name
            )

        except Exception as exc:
            logger.exception("Failed to load OpenCLIP model.")

            raise RuntimeError(
                f"Unable to initialize OpenCLIP: {exc}"
            ) from exc

        self._model = model.to(self.device).eval()
        self._transform = preprocess
        self._tokenizer = tokenizer

        logger.info(
            f"Loaded OpenCLIP model '{self.model_name}'."
        )

    def _prepare_text_embeddings(self) -> None:
        """Precompute and cache text embeddings."""
        self._labels.clear()
        self._label_to_category.clear()

        for category, labels in self.categories.items():
            for label in labels:
                self._labels.append(label)
                self._label_to_category[label] = category

        prompts = [
            f"a photo of a {label}"
            for label in self._labels
        ]

        tokens = self._tokenizer(prompts).to(self.device)

        with torch.inference_mode():
            text_features = self._model.encode_text(tokens)

            self._text_features = (
                text_features
                / text_features.norm(
                    dim=-1,
                    keepdim=True,
                )
            )

        logger.info(
            f"Cached {len(self._labels)} CLIP text embeddings."
        )

    def _warmup_model(self) -> None:
        """Run a single inference to initialize CUDA kernels."""
        dummy_image = Image.new(
            "RGB",
            (224, 224),
            color="white",
        )

        image_tensor = self._transform(dummy_image)

        image_tensor = (
            image_tensor
            .unsqueeze(0)
            .to(self.device)
        )

        with torch.inference_mode():
            with torch.autocast(
                device_type=self.device.type,
                enabled=self.device.type == "cuda",
            ):
                image_features = (
                    self._model.encode_image(
                        image_tensor
                    )
                )

                image_features = (
                    image_features
                    / image_features.norm(
                        dim=-1,
                        keepdim=True,
                    )
                )

                _ = (
                    100.0
                    * image_features
                    @ self._text_features.T
                ).softmax(dim=-1)

        logger.info("OpenCLIP warmup completed.")

    def _validate_image(
        self,
        image: Image.Image | bytes | BytesIO,
    ) -> Image.Image:
        """Validate supported image types."""
        if isinstance(
            image,
            (bytes, bytearray),
        ):
            image = Image.open(
                BytesIO(image)
            )

        elif isinstance(
            image,
            BytesIO,
        ):
            image = Image.open(image)

        if not isinstance(
            image,
            Image.Image,
        ):
            raise TypeError(
                "Expected PIL.Image, bytes, or BytesIO."
            )

        image.load()

        return convert_to_rgb(image)

    def _preprocess(
        self,
        image: Image.Image,
    ) -> torch.Tensor:
        """Apply OpenCLIP preprocessing."""
        return (
            self._transform(image)
            .unsqueeze(0)
            .to(self.device)
        )

    def _predict(
        self,
        image_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Run CLIP inference using cached text embeddings."""
        with torch.inference_mode():
            with torch.autocast(
                device_type=self.device.type,
                enabled=self.device.type == "cuda",
            ):
                image_features = (
                    self._model.encode_image(
                        image_tensor
                    )
                )

                image_features = (
                    image_features
                    / image_features.norm(
                        dim=-1,
                        keepdim=True,
                    )
                )

                similarity = (
                    100.0
                    * image_features
                    @ self._text_features.T
                )

                probabilities = similarity.softmax(
                    dim=-1
                )

        return probabilities.squeeze(0)

    def classify(
        self,
        image: Image.Image | bytes | BytesIO,
        top_k: int | None = None,
    ) -> dict[str, Any]:
        """Classify a single image."""
        validated_image = self._validate_image(image)

        image_tensor = self._preprocess(validated_image)

        probabilities = self._predict(image_tensor)

        return self._postprocess(
            probabilities=probabilities,
            top_k=top_k,
        )

    def classify_batch(
        self,
        images: list[Image.Image | bytes | BytesIO],
        top_k: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Classify multiple images sequentially.

        This method provides a clean public API for batch inference.
        Future versions can replace the internal loop with true
        batched GPU inference without changing external callers.
        """
        results: list[dict[str, Any]] = []

        for image in images:
            results.append(
                self.classify(
                    image=image,
                    top_k=top_k,
                )
            )

        return results

    def _category_confidence(
        self,
        probabilities: torch.Tensor,
    ) -> dict[str, float]:
        """Total probability mass each category attracted.

        Summed over every label in the category, not just the top-k, so the
        result is a genuine probability distribution over categories.
        """
        totals: dict[str, float] = {
            category: 0.0
            for category in self.categories
        }

        for label, probability in zip(
            self._labels,
            probabilities.tolist(),
        ):
            totals[self._label_to_category[label]] += float(probability)

        return totals

    def _postprocess(
        self,
        probabilities: torch.Tensor,
        top_k: int | None = None,
    ) -> dict[str, Any]:
        """Convert CLIP probabilities into a structured response.

        The accept/reject decision is made on the winning category's total
        probability mass, NOT on the top-1 label's probability.

        The reason is that these probabilities come from a softmax over every
        label in the catalogue, so they measure how alone the winning label is
        among its neighbours — a property of DEFAULT_CATEGORIES, not of the
        photo. Two labels for near-identical concepts split the mass between
        them and both look uncertain even when the model is sure. Measured on
        this project's test images: television.jpg put 0.6142 on "television"
        and 0.3809 on "monitor", so the old top-1 gate of 0.75 rejected a
        correct prediction; car.jpg, whose raw similarity to its label was the
        *lowest* of all six images, scored 0.9805 purely because "car" has no
        synonym in the catalogue. Top-1 probability ran opposite to match
        quality.

        That failure gets worse as the catalogue grows. Adding "smart tv"
        alongside "television" would split the mass three ways and start
        rejecting images that used to pass, with no test failing and no
        obvious connection between editing a label list and TVs no longer
        verifying. Category mass is immune to it: near-synonyms almost always
        sit in the same category, so adding one moves mass around inside the
        category total without changing it. television.jpg scores 0.9970 by
        that measure. It is also the decision the platform actually needs —
        a lister picks a category, and nobody needs this service to
        adjudicate television versus monitor.

        The specific label is still returned, just not used as the gate.
        """
        top_k = (
            top_k
            if top_k is not None
            else settings.ai.top_k_results
        )

        top_k = max(
            1,
            min(
                top_k,
                len(self._labels),
            ),
        )

        threshold = settings.ai.category_confidence_threshold

        category_confidence = self._category_confidence(
            probabilities
        )

        values, indices = torch.topk(
            probabilities,
            top_k,
        )

        predictions: list[dict[str, Any]] = []

        for value, index in zip(values, indices):
            idx = int(index.item())

            label = self._labels[idx]

            confidence = float(value.item())

            predictions.append(
                {
                    "label": label.capitalize(),
                    "category": self._label_to_category[label],
                    "confidence": round(
                        confidence,
                        4,
                    ),
                }
            )

        best_prediction = predictions[0]

        winning_category_confidence = category_confidence[
            best_prediction["category"]
        ]

        if winning_category_confidence < threshold:
            best_prediction = {
                "label": "Unknown",
                "category": "Unknown",
                "confidence": best_prediction["confidence"],
            }

        return {
            "label": best_prediction["label"],
            "category": best_prediction["category"],
            "confidence": best_prediction["confidence"],
            # Reported even when the verdict is Unknown: this is the number
            # that decided it, so the caller can apply a stricter policy of
            # its own without re-running inference.
            "category_confidence": round(
                winning_category_confidence,
                4,
            ),
            "predictions": predictions,
            "model": self.model_name,
            "device": str(self.device),
        }


__all__ = (
    "ImageClassifier",
    "DEFAULT_CATEGORIES",
)