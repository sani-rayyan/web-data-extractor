import json
from pathlib import Path
from config import OUTPUT_JSON


def save_json(rows: list[dict]) -> None:
    if not rows:
        return

    Path(OUTPUT_JSON).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
        



