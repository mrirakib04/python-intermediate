# advanced_functions.py


# 1. *args and **kwargs
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


print_args(1, 2, 3, name="Rakib", age=18)


# 2. Recursive function (factorial)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))


# 3. Closures & higher-order functions
def outer_function(msg):
    def inner_function():
        print("Message:", msg)

    return inner_function


my_func = outer_function("Hello from closure!")
my_func()


# 4. Decorators
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


@my_decorator
def say_hello():
    print("Hello, Rakib!")


say_hello()
