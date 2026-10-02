# How to define and call a function
def greet(name):
    print(f"Hello, {name}!")


greet('Jane')

# Using default parameter values


def square(x):
    return x * x


print(square(5))

# Using default parameter values


def greet(name="World"):
    print(f"Hello, {name}!")


greet()

# Using keyword arguments


def greet_keyword(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet_keyword(name="John", greeting="Hi")   # output: Hi, John!

# Using variable-length argument lists


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(multiply(2, 3, 4))   # output: 24
print(multiply(5, 10))     # output: 50

# Using lambda functions


def square(x): return x * x


print(square(3))

fruits = [('apple', 10), ('banana', 5), ('cherry', 20)]
fruits.sort(key=lambda fruit: fruit[1])
print(fruits)  # Output: [('banana', 5), ('apple', 10), ('cherry', 20)]

numbers = [5, 8, 2, 10, 3]
max_number = max(numbers, key=lambda x: x)
print(max_number)  # Output: 10

# Passing functions as arguments


def apply(func, x):
    return func(x)


def square2(x):
    return x * x


result = apply(square2, 5)
print(result)   # output: 25

# Using closures


def add(x):
    def inner(y):
        return x + y
    return inner


add5 = add(5)
result = add5(3)
print(result)   # output: 8

# Using decorators


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("John")
