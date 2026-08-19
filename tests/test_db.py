import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sqlalchemy import create_engine, text
from app.config.settings import settings

engine = create_engine(settings.database.url)

try:
    with engine.connect() as conn:
        print("✅ Successfully connected to MySQL!")

        result = conn.execute(text("SELECT DATABASE();"))
        print("Current Database:", result.scalar())

        result = conn.execute(text("SHOW TABLES;"))

        print("\nTables:")
        for table in result:
            print("-", table[0])

except Exception as e:
    print("❌ Connection Failed")
    print(e)