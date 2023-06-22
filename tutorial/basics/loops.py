# For loops
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# While loops
num = 6
while num <= 11:
    print(num)
    num += 1

# Nested Loops
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in list_of_lists:
    for item in sublist:
        print(item)

# Loop Control Statements

# break
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

# continue
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
print(squares)

# Use cases for loops

# Summing a list of numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)

# Printing a multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()

# Finding the first prime number
num = 2
while True:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        break
    num += 1
