import json
from pathlib import Path

def load_data():
    """
    Load preprocessed NASA bio data from JSON file.
    """
    data_path = Path("data/nasa_bio_data.json")
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path.resolve()}")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load_data()

