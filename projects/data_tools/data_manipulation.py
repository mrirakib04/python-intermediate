# Data Manipulation with Built-in Modules

numbers = [10, 20, 30, 40, 50]
print("--- Data Manipulation ---")
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))

# Sorting
words = ["python", "rakib", "banana", "apple"]
print("Sorted words:", sorted(words))

# Dictionary sorting
scores = {"Rakib": 90, "Rahim": 85, "Karim": 95}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print("Sorted scores:", sorted_scores)
