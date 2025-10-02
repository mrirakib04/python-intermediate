# libraries_examples.py

import datetime
import time
import os
import sys
from collections import Counter, defaultdict, namedtuple

# ----------------------------
# 1. datetime & time
# ----------------------------
print("--- datetime & time ---")
now = datetime.datetime.now()
print("Current date & time:", now)

# Formatting
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Sleep example
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done waiting!")

# Date arithmetic
tomorrow = now + datetime.timedelta(days=1)
print("Tomorrow:", tomorrow.date())


# ----------------------------
# 2. os & sys
# ----------------------------
print("\n--- os & sys ---")
print("Current working dir:", os.getcwd())
print("Files in dir:", os.listdir("."))

# Environment variables
print("Home directory:", os.environ.get("HOME"))

# Command line args (sys.argv)
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])  # if you pass extra args when running script


# ----------------------------
# 3. collections module
# ----------------------------
print("\n--- collections ---")

# Counter
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = Counter(nums)
print("Counter:", count)

# defaultdict
dd = defaultdict(int)
dd["apple"] += 1
dd["banana"] += 2
print("Defaultdict:", dict(dd))

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(10, 20)
print("NamedTuple:", p1.x, p1.y)
