# functional_programming.py

from functools import reduce

# ----------------------------
# 1. map(), filter(), reduce()
# ----------------------------

# map() → apply function to each element
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("--- map() Example ---")
print(squares)  # [1, 4, 9, 16, 25]

# filter() → keep only elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("\n--- filter() Example ---")
print(evens)  # [2, 4]

# reduce() → combine elements into a single result
total = reduce(lambda x, y: x + y, numbers)
print("\n--- reduce() Example ---")
print(total)  # 15


# ----------------------------
# 2. List & Generator Comprehensions
# ----------------------------

# List comprehension
cubes = [x**3 for x in numbers]
print("\n--- List Comprehension ---")
print(cubes)  # [1, 8, 27, 64, 125]

# Generator comprehension
gen = (x**2 for x in range(6))
print("\n--- Generator Comprehension ---")
for val in gen:
    print(val, end=" ")  # 0 1 4 9 16 25
print()


# ----------------------------
# 3. Immutability Concepts
# ----------------------------

# Tuples are immutable (cannot be changed)
my_tuple = (1, 2, 3)
print("\n--- Immutability Example ---")
print("Original tuple:", my_tuple)

try:
    my_tuple[0] = 99  # This will raise error
except TypeError as e:
    print("Error:", e)

# Strings are also immutable
text = "Rakib"
new_text = text.replace("R", "M")  # creates new string
print("Original string:", text)
print("Modified string:", new_text)
