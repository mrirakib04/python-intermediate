# modules_packages_demo.py

# ----------------------------
# 1. Creating custom module (simulate)
# ----------------------------
# Normally we save this in math_utils.py
# but here we just define it inside one file.


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b


# ----------------------------
# 2. Simulating __init__.py (package style)
# ----------------------------
# In real projects, __init__.py exposes functions.
# Here we mimic that using another class.


class MyPkg:
    from_this_pkg = "This simulates __init__.py"
    add = MathUtils.add
    mul = MathUtils.mul

    @staticmethod
    def upper_case(s):
        return s.upper()


# ----------------------------
# 3. Virtual environment & pip (demo only)
# ----------------------------
# Can't actually run pip/venv commands in Python file,
# but we show them as strings for reference.


def show_venv_and_pip():
    commands = [
        "python -m venv venv",
        "venv\\Scripts\\activate   # Windows",
        "source venv/bin/activate  # Linux/Mac",
        "pip install requests",
        "pip freeze > requirements.txt",
        "pip install -r requirements.txt",
    ]
    return "\n".join(commands)


# ----------------------------
# Usage
# ----------------------------
print("--- Custom Module ---")
print("Add:", MathUtils.add(2, 3))
print("Mul:", MathUtils.mul(4, 5))

print("\n--- Package Simulation (__init__.py) ---")
print("Add from pkg:", MyPkg.add(10, 20))
print("Upper from pkg:", MyPkg.upper_case("rakib"))

print("\n--- Virtual Env & pip Commands ---")
print(show_venv_and_pip())
