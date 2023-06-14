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
