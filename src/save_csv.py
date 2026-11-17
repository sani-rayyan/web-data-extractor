import csv
from pathlib import Path
from config import OUTPUT_CSV


def save_csv(rows: list[dict]) -> None:
    if not rows:
        return
    Path(OUTPUT_CSV).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
        