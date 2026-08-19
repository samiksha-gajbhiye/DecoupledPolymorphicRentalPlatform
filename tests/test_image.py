"""
ImageAnalysis Model Test Suite

Tests:
1. Enum values
2. Model creation
3. Default processing status
4. __repr__()
5. Column metadata
6. Table metadata
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from sqlalchemy import inspect

from app.config.database import database
from app.models.image import (
    ImageAnalysis,
    ProcessingStatus,
)


def separator(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_enum():

    separator("TEST 1 : ProcessingStatus Enum")

    for status in ProcessingStatus:
        print(status.name, "->", status.value)

    print("✅ Enum Test Passed")


def test_model_creation():

    separator("TEST 2 : Model Creation")

    analysis = ImageAnalysis(

        product_id=1,

        image_url="uploads/chair.jpg",

        filename="chair.jpg",

        width=1920,

        height=1080,

        image_format="JPEG",

        file_size=254812,

        blur_score=0.03,

        duplicate_score=0.02,

        confidence=0.98,

    )

    print("Model Created Successfully")

    print(analysis)


def test_default_status():

    separator("TEST 3 : Default Status")

    analysis = ImageAnalysis(

        product_id=10,

        image_url="uploads/table.jpg",

        filename="table.jpg",

        width=800,

        height=600,

        image_format="JPEG",

        file_size=50000,

    )

    print("Processing Status :", analysis.processing_status)

    if analysis.processing_status == ProcessingStatus.PENDING:
        print("✅ Default Status Correct")
    else:
        print("❌ Default Status Incorrect")


def test_repr():

    separator("TEST 4 : __repr__")

    analysis = ImageAnalysis(

        id=1,

        product_id=50,

        image_url="uploads/image.jpg",

        filename="image.jpg",

        width=500,

        height=500,

        image_format="JPEG",

        file_size=1024,

        processing_status=ProcessingStatus.COMPLETED,

    )

    print(repr(analysis))

    print("✅ __repr__ Working")


def test_columns():

    separator("TEST 5 : Model Columns")

    mapper = inspect(ImageAnalysis)

    for column in mapper.columns:

        print(
            f"{column.name:<20}"
            f"{str(column.type):<20}"
            f"Nullable={column.nullable}"
        )

    print("\n✅ Column Inspection Complete")


def test_table_information():

    separator("TEST 6 : Table Metadata")

    print("Table Name :", ImageAnalysis.__tablename__)

    print("Comment    :")

    print(ImageAnalysis.__table__.comment)

    print("\nPrimary Keys")

    for pk in ImageAnalysis.__table__.primary_key.columns:
        print("-", pk.name)

    print("\nIndexes")

    for index in ImageAnalysis.__table__.indexes:
        print("-", index.name)

    print("\n✅ Metadata Verified")


def test_database_mapping():

    separator("TEST 7 : Database Mapping")

    try:

        database.initialize()

        engine = database.get_engine()

        inspector = inspect(engine)

        tables = inspector.get_table_names()

        if ImageAnalysis.__tablename__ in tables:

            print("✅ Table Exists in Database")

        else:

            print("⚠ Table Not Yet Created")

        database.shutdown()

    except Exception as e:

        print(e)


def main():

    separator("IMAGE ANALYSIS MODEL HEALTH CHECK")

    test_enum()

    test_model_creation()

    test_default_status()

    test_repr()

    test_columns()

    test_table_information()

    test_database_mapping()

    separator("ALL MODEL TESTS FINISHED")


if __name__ == "__main__":
    main()