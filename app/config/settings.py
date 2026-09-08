# Application settings
import os
from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from dotenv import load_dotenv
load_dotenv()


def _require_env(var_name: str) -> str:
    value = os.environ.get(var_name)
    if not value:
        raise RuntimeError(
            f"Missing required environment variable '{var_name}'.\n"
            f"Add it to your .env file at the project root, e.g.:\n"
            f"  {var_name}=some-long-random-string\n"
            f"(For local dev, any random string works — just don't commit it.)"
        )
    return value

class AppConfig(BaseModel):
    name: str
    version: str
    description: str
    api_prefix: str
    environment: str
    debug: bool

class RedisConfig(BaseModel):
    host: str = "localhost"
    port: int = 6379
    db: int = 0

class UploadConfig(BaseModel):
    upload_directory: Path = Path("uploads")
    temp_directory: Path = Path("tmp")
    max_image_size: int = 5242880
    allowed_image_formats: list[str] = Field(default_factory=lambda: ["jpg", "jpeg"])
    allowed_document_formats: list[str] = Field(default_factory=lambda: ["pdf"])

class AIConfig(BaseModel):
    clip_model_name: str = "ViT-B-32"
    clip_pretrained: str = "openai"
    clip_directory: Path = Path("models/clip")
    yolo_directory: Path = Path("models/yolo")
    yolo_model: Path = Path("models/yolo/weights/yolo11n.pt")
    yolo_confidence: float = 0.25
    yolo_iou_threshold: float = 0.45
    yolo_max_detections: int = 100
    # Calibrated 2026-08-27: sharp >= 596, blurry <= 386 (measured at 512px, downscale-only)
    blur_threshold: float = 450.0
    blur_normalize_edge: int = 512
    # Calibrated 2026-09-08: same-image variants <= 90, different images >= 110 (hash_size=16)
    duplicate_threshold: int = 95
    duplicate_hash_size: int = 16
    embedding_model: str = "all-MiniLM-L6-v2"
    sentence_transformer_directory: Path = Path("models/sentence_transformers")
    vector_database: Path = Path("app/ml/vector_db")
    checkpoint_directory: Path = Path("app/ml/checkpoints")
    model_directory: Path = Path("models")
    # Classification gate. Applied to the total probability mass of the winning
    # CATEGORY, not to the top-1 label — see ImageClassifier._postprocess for why
    # a top-1 label probability is not a usable confidence here.
    # Calibrated 2026-09-04 against test_images/ plus six synthetic junk uploads
    # (noise, blank, solid grey, a document, a dark smear, an extreme close-up):
    # real items scored >= 0.9222, junk <= 0.7727.
    category_confidence_threshold: float = 0.85
    top_k_results: int = 5
    device: str = "cuda"

class SecurityConfig(BaseModel):
    jwt_secret: str
    jwt_algorithm: str
    access_token_expire: int

class LoggingConfig(BaseModel):
    level: str = "INFO"
    log_directory: Path = Path("logs")
    log_file: str = "app.log"
    rotation: str = "500 MB"
    retention: str = "10 days"

class Settings(BaseSettings):
    # env_nested_delimiter lets nested values be overridden from .env without a
    # code change, e.g. AI__BLUR_THRESHOLD=500 to re-tune the blur gate.
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_nested_delimiter="__",
    )

    application: AppConfig = AppConfig(
        name="Rentify",
        version="1.0.0",
        description="AI Microservice",
        api_prefix="/api/v1",
        environment="development",
        debug=True
    )

    redis: RedisConfig = RedisConfig()
    upload: UploadConfig = UploadConfig()
    ai: AIConfig = AIConfig()

    security: SecurityConfig = SecurityConfig(
        jwt_secret=_require_env("JWT_SECRET"),
        jwt_algorithm="HS256",
        access_token_expire=36000000
    )

    logging: LoggingConfig = LoggingConfig()

settings = Settings()