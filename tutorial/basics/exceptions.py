# ZeroDivisionError

try:
    x = 0
    y = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("The result is:", y)
finally:
    print("Done.")

# TypeError
a = 10
b = "20"
try:
    result = a + b
except TypeError as e:
    print("Error:", e)

# ValueError
try:
    number = int("abc")
except ValueError as e:
    print("Error:", e)

# KeyError
my_dict = {"name": "John", "age": 25}
try:
    value = my_dict["address"]
except KeyError as e:
    print("Key Error:", e)

# IndexError
my_list = [1, 2, 3]
try:
    value = my_list[5]
except IndexError as e:
    print("Index Error:", e)

# FileNotFoundError
try:
    file = open("nonexistent_file.txt", "r")
except FileNotFoundError as e:
    print("File not found Error:", e)

# ImportError
try:
    import non_existent_module
except ImportError as e:
    print("Import Error:", e)

# KeyboardInterupt
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted by the user.")

# General exception
try:
    x = 10 / 0
except Exception as e:
    print("An exception occurred:", e)
