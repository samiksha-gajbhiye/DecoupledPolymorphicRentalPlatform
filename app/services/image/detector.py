# Image detector service
from __future__ import annotations
from io import BytesIO
from pathlib import Path
from typing import Any
from PIL import Image
from ultralytics import YOLO
from app.config.logger import logger
from app.config.settings import settings
from app.utils.image_utils import convert_to_rgb
 
 
class ImageDetector:
    """YOLO-based object detector for product images.
    detect() is the only public method. The model is loaded and
    warmed up once in __init__, never per request. Unlike
    ImageClassifier, no candidate labels are needed — YOLO carries
    its own class names from training (e.g. COCO: chair, couch,
    laptop, tv, car, ...).
    """
    def __init__(
        self,
        model_path: str | None = None,
        confidence: float | None = None,
        iou_threshold: float | None = None,
        max_detections: int | None = None,
        device: str | None = None,
    ) -> None:
        """Load configuration from settings.ai unless explicitly overridden. 
        Args:
            model_path: Path to a YOLO .pt weights file.
            confidence: Minimum confidence to keep a detection, 0-1.
            iou_threshold: IoU threshold used by YOLO's NMS step.
            max_detections: Maximum objects returned per image.
            device: "cpu" or "cuda". Falls back to cpu if cuda is
                requested but unavailable.
        """
        self.model_path = model_path or settings.ai.yolo_model
        self.confidence = confidence if confidence is not None else settings.ai.yolo_confidence
        self.iou_threshold = (
            iou_threshold if iou_threshold is not None else settings.ai.yolo_iou_threshold
        )
        self.max_detections = (
            max_detections if max_detections is not None else settings.ai.yolo_max_detections
        )
        requested_device = device or settings.ai.device
        if requested_device == "cuda":
            try:
                import torch
                if not torch.cuda.is_available():
                    requested_device = "cpu"
            except ImportError:
                requested_device = "cpu"
        self.device = requested_device
 
        self._model: YOLO | None = None
        self._load_model()
        self._warmup_model()
    def _load_model(self) -> None:
        """Load the YOLO model from settings.ai.yolo_model.
        Fails loudly and clearly if the weight file is missing, rather
        than letting Ultralytics silently attempt an auto-download or
        raise a bare FileNotFoundError deep in its internals.
        """
        model_file = Path(self.model_path)
        if not model_file.is_file():
            raise RuntimeError(
                f"YOLO model file not found: '{self.model_path}'. "
                "Set settings.ai.yolo_model to a valid weights path."
            )
        logger.info(f"Loading YOLO model: {model_file.name}")
        try:
            self._model = YOLO(str(model_file))
        except Exception as exc:
            logger.error(f"Failed to load YOLO model: {exc}")
            raise RuntimeError(f"Unable to load YOLO model '{self.model_path}': {exc}") from exc

        logger.info(f"YOLO device: {self.device}")
        logger.info("YOLO model loaded successfully.")
 
    def _warmup_model(self) -> None:
        """Run one dummy inference so the first real request doesn't
        pay YOLO's cold-start cost.
        """
        dummy_image = Image.new("RGB", (224, 224), color="white")
        try:
            self._model.predict(source=dummy_image, device=self.device, verbose=False)
        except Exception as exc:
            logger.error(f"YOLO warmup failed: {exc}")
            raise RuntimeError(f"YOLO warmup failed: {exc}") from exc
        logger.info("YOLO model warmed up.")
 
    def _validate_image(self, image: Image.Image | bytes | BytesIO) -> Image.Image:
        """Accept PIL.Image, bytes, or BytesIO and return an RGB
        PIL.Image. Reuses convert_to_rgb() from image_utils rather
        than duplicating that logic — same contract as classifier.py.
        """
        if isinstance(image, (bytes, bytearray)):
            image = Image.open(BytesIO(image))
        elif isinstance(image, BytesIO):
            image = Image.open(image)
 
        if not isinstance(image, Image.Image):
            raise TypeError(f"Expected PIL.Image, bytes, or BytesIO, got {type(image)!r}.")
 
        image.load()
        return convert_to_rgb(image)
 
    def detect(self, image: Image.Image | bytes | BytesIO) -> dict[str, Any]:
        """Detect objects in an image.
 
        Args:
            image: A PIL Image, raw bytes, or a BytesIO buffer.
 
        Returns:
            {
                "objects": [
                    {"label": str, "confidence": float, "bbox": [x1, y1, x2, y2]},
                    ...
                ],
                "object_count": int,
            }
        """
        validated_image = self._validate_image(image)
        logger.debug("Running YOLO detection.")
        result = self._run_detection(validated_image)
        return self._postprocess(result)
 
    def _run_detection(self, image: Image.Image):
        """Run YOLO inference with the configured confidence, IoU, and
        max-detections thresholds. NMS (deduplicating overlapping boxes
        via IoU) is handled internally by YOLO — not reimplemented here.
        """
        try:
            results = self._model.predict(
                source=image,
                conf=self.confidence,
                iou=self.iou_threshold,
                max_det=self.max_detections,
                device=self.device,
                verbose=False,
            )
        except Exception as exc:
            logger.error(f"YOLO inference failed: {exc}")
            raise RuntimeError(f"YOLO inference failed: {exc}") from exc
        return results[0]
 
    def _postprocess(self, result) -> dict[str, Any]:
        """Convert Ultralytics' Results object into the application's
        plain-dict contract. Callers never need to know how
        Ultralytics represents detections internally.
        """
        class_names = result.names
        objects = []
        for box in result.boxes:
            class_id = int(box.cls.item())
            confidence_pct = round(float(box.conf.item()) * 100, 1)
            bbox = [round(coord, 1) for coord in box.xyxy[0].tolist()]
            objects.append(
                {
                    "label": class_names[class_id],
                    "confidence": confidence_pct,
                    "bbox": bbox,
                }
            )
 
        logger.debug(f"Detected {len(objects)} object(s).")
        return {"objects": objects, "object_count": len(objects)}
 
 
__all__ = ("ImageDetector",)