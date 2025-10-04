import json
from pathlib import Path

def load_data():
    data_path = Path("data/nasa_bio_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load_data()
