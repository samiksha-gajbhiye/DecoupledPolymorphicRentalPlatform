import sys
from pathlib import Path
from loguru import logger
from app.config.settings import settings

# Use the Directory from Settings dynamically
LOG_DIR = settings.logging.log_directory
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Remove Default Logger
logger.remove()

# Fixed Console Logger 
logger.add(
    sink=sys.stderr,
    level=settings.logging.level,
    colorize=True,
    enqueue=True, 
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level:<8}</level> | "
        "<cyan>{name}</cyan>:"
        "<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
)

# Dynamic Application Log
logger.add(
    LOG_DIR / settings.logging.log_file,
    level="INFO",
    rotation=settings.logging.rotation,
    retention=settings.logging.retention,
    compression="zip",
    enqueue=True,
)

# Error Log 
logger.add(
    LOG_DIR / "error.log",
    level="ERROR",
    rotation=settings.logging.rotation,
    retention="60 days",  
    compression="zip",
    enqueue=True,
)

# Export Logger
__all__ = ["logger"]