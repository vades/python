# an example of a simple class in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)


person1 = Person("John", 25)
person1.say_hello()  # Output: Hello, my name is John

# Creating a Rectangle Class


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(5, 10)
print(r.area())  # Output: 50
print(r.perimeter())  # Output: 30

# Creating a Calculator Class


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


c = Calculator()
print(c.add(5, 10))  # Output: 15
print(c.subtract(10, 5))  # Output: 5
print(c.multiply(3, 4))  # Output: 12
print(c.divide(10, 2))  # Output: 5.0
