import os
from pathlib import Path

cache = Path.home() / ".cache"

for root, dirs, files in os.walk(cache):
    for file in files:
        if "ViT" in file or "clip" in file.lower() or file.endswith(".pt") or file.endswith(".bin"):
            print(os.path.join(root, file))