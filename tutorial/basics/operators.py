""" Arithmetic Operators: """
a = 10
b = 5

# Addition
c = a + b
print(c)  # Output: 15

# Subtraction
c = a - b
print(c)  # Output: 5

# Multiplication
c = a * b
print(c)  # Output: 50

# Division
c = a / b
print(c)  # Output: 2.0

# Modulo
c = a % b
print(c)  # Output: 0

# Exponentiation
c = a ** b
print(c)  # Output: 100000

""" Comparison Operators """
a = 10
b = 5

# Equal to
c = (a == b)
print(c)  # Output: False

# Not equal to
c = (a != b)
print(c)  # Output: True

# Greater than
c = (a > b)
print(c)  # Output: True

# Less than
c = (a < b)
print(c)  # Output: False

# Greater than or equal to
c = (a >= b)
print(c)  # Output: True

# Less than or equal to
c = (a <= b)
print(c)  # Output: False

""" Logical Operators """
a = True
b = False

# Logical AND
c = (a and b)
print(c)  # Output: False

# Logical OR
c = (a or b)
print(c)  # Output: True

# Logical NOT
c = (not a)
print(c)  # Output: False

""" Assignment Operators: """
a = 10

# Add and assign
a += 5
print(a)  # Output: 15

# Subtract and assign
a -= 5
print(a)  # Output: 10

# Multiply and assign
a *= 2
print(a)  # Output: 20

# Divide and assign
a /= 2
print(a)  # Output: 10.0

# Modulo and assign
a %= 3
print(a)  # Output: 1.0

# Exponentiate and assign
a **= 2
print(a)  # Output: 1.0

""" Membership Operators: """
a = [1, 2, 3]

# In operator
b = 2 in a
print(b)  # Output: True

# Not in operator
b = 4 not in a
print(b)  # Output: True

""" Identity Operators: """
a = [1, 2, 3]
b = a

# is operator
c = a is b
print(c)  # Output: True

# is not operator
c = a is not b
print(c)  # Output: False

""" Bitwise Operators: """
a = 60    # 60 = 0011 1100
b = 13    # 13 = 0000 1101

# Bitwise AND
c = a & b   # 12 = 0000 1100
print(c)  # Output: 12

# Bitwise OR
c = a | b   # 61 = 0011 1101
print(c)  # Output: 61

# Bitwise XOR
c = a ^ b   # 49 = 0011 0001
print(c)  # Output: 49

# Bitwise NOT
c = ~a  # -61 = 1100 0011
print(c)  # Output: -61

# Left shift
c = a << 2  # 240 = 1111 0000
print(c)  # Output: 240

# Right shift
c = a >> 2  # 15 = 0000 1111
print(c)  # Output: 15
