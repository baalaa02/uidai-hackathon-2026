import json
import csv
from collections import Counter

INPUT_FILE = "phase2/results/insights_per_repo.json"

def normalize(text):
    return text.lower().strip()

def run():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_insights = []

    for entry in data:
        bullets = entry["insights"].split("\n")
        for b in bullets:
            b = b.strip("-• ").strip()
            if len(b) > 10:
                all_insights.append(normalize(b))

    counter = Counter(all_insights)

    with open("phase2/results/insight_frequency.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["insight", "count"])
        for insight, count in counter.most_common():
            writer.writerow([insight, count])

    with open("phase2/results/insight_clusters.md", "w", encoding="utf-8") as f:
        f.write("# Aggregated Insights\n\n")
        for insight, count in counter.most_common():
            f.write(f"- **({count})** {insight}\n")

    print("Aggregation complete.")

if __name__ == "__main__":
    run()
