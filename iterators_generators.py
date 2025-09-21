# iterators_generators.py

# 1. iter() and next()
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))  # StopIteration error


# 2. Custom Iterator
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


cd = Countdown(5)
for num in cd:
    print(num)  # 5 4 3 2 1


# 3. Generator Function with yield
def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i


gen = square_numbers(5)
for val in gen:
    print(val)  # 1 4 9 16 25


# 4. Generator Expression
gen_exp = (x * 2 for x in range(5))
for val in gen_exp:
    print(val)  # 0 2 4 6 8
