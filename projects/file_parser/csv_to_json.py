import csv
import json

csv_file = "sample.csv"
json_file = "sample.json"

# Write sample CSV
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Rakib", "age": 18})
    writer.writerow({"name": "Rahim", "age": 20})

# Read CSV -> JSON
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open(json_file, "w") as f:
    json.dump(data, f, indent=2)

print(f"Converted {csv_file} -> {json_file}")
