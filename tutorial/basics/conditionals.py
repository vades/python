# Check if a number is positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is negative")

# Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Check if a student has passed or failed an exam
score = int(input("Enter your exam score: "))
if score >= 60:
    print("Congratulations, you have passed the exam!")
else:
    print("Sorry, you have failed the exam.")

# Logical operators
# and
x = 5
y = 10
z = 15

if x > 0 and y > 0:
    print("Both x and y are positive")

# or
name = "Bob"
age = 15

if name == "Alice" or age >= 18:
    print("Welcome, Alice! You are old enough.")
else:
    print("Sorry, you must be Alice or at least 18 years old.")

# not
age = 25

if not (age >= 18):
    print("You are not old enough.")

# Nested conditionals

# Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Ternary operator

# Check if a number is even or odd (using ternary operator)
num = int(input("Enter a number: "))
result = "even" if num % 2 == 0 else "odd"
print(f"The number is {result}")
