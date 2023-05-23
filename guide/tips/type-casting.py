# The `int()` function converts a value to an integer.
x = int(3.14)
print(x)  # Output: 3

y = int("5")
print(y)  # Output: 5

# The `float()` function converts a value to a floating-point number.
x = float(5)
print(x)  # Output: 5.0

y = float("3.14")
print(y)  # Output: 3.14

# The `str()` function converts a value to a string.
x = str(5)
print(x)  # Output: "5"

y = str(3.14)
print(y)  # Output: "3.14"

# The `bool()` function converts a value to a boolean.
x = bool(1)
print(x)  # Output: True

y = bool(0)
print(y)  # Output: False

# The `list()`, `tuple()`, and `set()` functions can be used to convert an iterable (such as a string or a range) to a list, tuple, or set, respectively.
x = list("Hello")
print(x)  # Output: ['H', 'e', 'l', 'l', 'o']

y = tuple(range(5))
print(y)  # Output: (0, 1, 2, 3, 4)

z = set([1, 2, 3, 2, 1])
print(z)  # Output: {1, 2, 3}
