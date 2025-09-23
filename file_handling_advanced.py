# file_handling_advanced.py

import csv
import json

# ----------------------------
# 1. Context Manager (with statement)
# ----------------------------
# 'with' automatically closes the file
with open("example.txt", "w") as f:
    f.write("Hello, this is Rakib!\n")
    f.write("Learning advanced file handling in Python.\n")

with open("example.txt", "r") as f:
    content = f.read()
    print("--- Text File Content ---")
    print(content)


# ----------------------------
# 2. Working with CSV
# ----------------------------
# Writing CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Rakib", 18])
    writer.writerow(["Rahim", 20])

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    print("\n--- CSV Content ---")
    for row in reader:
        print(row)


# ----------------------------
# 3. Working with JSON
# ----------------------------
data = {"name": "Rakib", "skills": ["Python", "React", "Node.js"]}

# Writing JSON
with open("data.json", "w") as f:
    json.dump(data, f)

# Reading JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print("\n--- JSON Content ---")
    print(loaded_data)


# ----------------------------
# 4. Handling Binary Files
# ----------------------------
# Writing binary (simulate an image or other binary data)
binary_data = bytes([65, 66, 67, 68])  # Represents ABCD in ASCII
with open("binary.bin", "wb") as f:
    f.write(binary_data)

# Reading binary
with open("binary.bin", "rb") as f:
    read_bytes = f.read()
    print("\n--- Binary File Content ---")
    print(read_bytes)
