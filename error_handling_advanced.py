# error_handling_advanced.py

# ----------------------------
# 1. Multiple except blocks
# ----------------------------
try:
    x = int("abc")  # ValueError
    y = 10 / 0  # ZeroDivisionError
except ValueError as ve:
    print("ValueError occurred:", ve)
except ZeroDivisionError as ze:
    print("ZeroDivisionError occurred:", ze)
except Exception as e:
    print("Other error:", e)


# ----------------------------
# 2. Custom Exceptions
# ----------------------------
class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed"""

    pass


def square_root(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return n**0.5


try:
    print("Square root:", square_root(25))
    print("Square root:", square_root(-9))  # Will raise custom exception
except NegativeNumberError as ne:
    print("Custom Exception:", ne)


# ----------------------------
# 3. Best Practices
# ----------------------------


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Both arguments must be numbers!")
        return None
    else:
        # Runs only if no exception occurred
        print("Division successful!")
        return result
    finally:
        # Always runs (cleanup logic here)
        print("Execution finished.")


print("\n--- Best Practices Example ---")
print("Result:", divide(10, 2))
print("Result:", divide(10, 0))
print("Result:", divide(10, "a"))
