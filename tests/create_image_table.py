import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

# IMPORTANT:
# Import the model before create_tables()
from app.models.image import ImageAnalysis

from app.config.database import database

database.initialize()

database.create_tables()

print("✅ create_tables() executed.")

database.shutdown()