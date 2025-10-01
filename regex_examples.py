# regex_examples.py

import re

# ----------------------------
# 1. Pattern Matching
# ----------------------------
print("--- Pattern Matching ---")
pattern = r"\d+"  # one or more digits
text = "My number is 12345 and my friend's is 67890"

matches = re.findall(pattern, text)
print("Digits found:", matches)  # ['12345', '67890']


# ----------------------------
# 2. Searching & Replacing
# ----------------------------
print("\n--- Searching & Replacing ---")
text2 = "I love Python. Python is awesome!"

# search first occurrence
match = re.search(r"Python", text2)
if match:
    print("First found at index:", match.start())

# replace all occurrences
replaced = re.sub(r"Python", "JavaScript", text2)
print("After replace:", replaced)


# ----------------------------
# 3. Practical Use Cases
# ----------------------------

# Email validation
print("\n--- Practical Use Case: Email Validation ---")
emails = ["test@example.com", "rakib@gmail", "hello@world.org"]
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

for email in emails:
    if re.match(email_pattern, email):
        print(email, "=> Valid")
    else:
        print(email, "=> Invalid")

# Extract hashtags from text
print("\n--- Practical Use Case: Extract Hashtags ---")
tweet = "Learning #Python with #Rakib. #Coding is fun!"
hashtags = re.findall(r"#\w+", tweet)
print("Hashtags:", hashtags)

# Phone number masking
print("\n--- Practical Use Case: Phone Masking ---")
phone = "01712345678"
masked = re.sub(r"\d{6}$", "******", phone)
print("Masked phone:", masked)
