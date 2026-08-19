import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)
from sqlalchemy import text

from app.config.database import database


def separator(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def run_database_health_check():
    separator("DATABASE HEALTH CHECK")

    try:
        print("\n[1] Initializing DatabaseManager...")
        database.initialize()
        print("✅ DatabaseManager initialized")

        print("\n[2] Creating Engine...")
        engine = database.get_engine()
        print("✅ Engine created")

        print("\n[3] Checking Connection...")
        if database.check_connection():
            print("✅ MySQL connection successful")
        else:
            print("❌ MySQL connection failed")
            return

        print("\n[4] Current Database")

        with engine.connect() as conn:
            current_db = conn.execute(
                text("SELECT DATABASE();")
            ).scalar()

            print(f"Database : {current_db}")

        print("\n[5] Tables")

        with engine.connect() as conn:
            tables = conn.execute(text("SHOW TABLES"))

            for table in tables:
                print(f"   ✓ {table[0]}")

        print("\n[6] Testing Session...")

        with database.get_session() as session:

            value = session.execute(
                text("SELECT 1")
            ).scalar()

            print(f"SELECT 1 returned : {value}")

            print("\n[7] Counting Rows")

            important_tables = [
                "user",
                "role",
                "product",
                "category",
                "address",
                "product_image",
            ]

            for table in important_tables:

                count = session.execute(
                    text(f"SELECT COUNT(*) FROM `{table}`")
                ).scalar()

                print(f"{table:<20} : {count}")

        print("\n✅ Session closed successfully")

        print("\n[8] Testing Ping...")

        if database.ping():
            print("✅ Ping Successful")
        else:
            print("❌ Ping Failed")

        print("\n[9] Testing Shutdown...")
        database.shutdown()
        print("✅ Engine disposed successfully")

        separator("DATABASE STATUS : HEALTHY")

    except Exception as e:

        separator("DATABASE STATUS : FAILED")
        print(type(e).__name__)
        print(e)


if __name__ == "__main__":
    run_database_health_check()