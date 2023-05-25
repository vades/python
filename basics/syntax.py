
import math
import math as m
from math import sqrt, pi

# The `print` function is used to display text in the console.
print("Hello", "World!")

# Python uses whitespace to indicate block structure.
if 5 > 2:
    print("Five is greater than two!")

# You can pass arguments to the function by enclosing them in parentheses
print("Hello, World!")

# Python uses indentation to denote block structure.


def greet(name):
    print("Hello, " + name + "!")


# You can import a module using the `import` statement.
# For example `import math`.
x = math.sqrt(16)
print(x)

# In this example, we import the `math` module under the alias `m`.
# For example: import math as m
x = m.sqrt(16)
print(x)

# You can also import a module under an alias using the `as` keyword, or import specific names from a module using the `from ... import` statement.
# For example: from math import sqrt, pi
x = sqrt(16)
print(x)

y = pi
print(y)

name = input("What is your name?\n ")
print("Hello, " + name + "!")
