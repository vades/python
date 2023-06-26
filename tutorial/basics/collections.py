"""
Lists
"""
fruits = ['apple', 'banana', 'cherry', 'date']

# Accessing elements
print(fruits[0])   # Output: 'apple'
print(fruits[3])   # Output: 'date'

# Modifying elements
fruits[1] = 'orange'
print(fruits)      # Output: ['apple', 'orange', 'cherry', 'date']

# List operations
fruits.append('grape')
fruits.remove('cherry')
print(fruits)      # Output: ['apple', 'orange', 'date', 'grape']

"""
Tuples
"""
person = ('John', 25, 'USA')
# Accessing elements
print(person[0])   # Output: 'John'
print(person[1])   # Output: 25

# Tuple packing and unpacking
name, age, country = person
print(name)        # Output: 'John'
print(age)         # Output: 25

# Errors

# person[1] = 30   # Error: 'tuple' object does not support item assignment
"""
Dictionaries
"""
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Accessing elements
print(student['name'])      # Output: 'Alice'
print(student.get('age'))   # Output: 20

# Modifying elements
student['grade'] = 'B'
# Output: {'name': 'Alice', 'age': 20, 'grade': 'B'}
print(student)

# Dictionary operations
student['school'] = 'XYZ High School'
del student['age']
# Output: {'name': 'Alice', 'grade': 'B', 'school': 'XYZ High School'}
print(student)
# Keys
# Getting all keys
keys = student.keys()
print(keys)

# Converting keys to a list
key_list = list(keys)
print(key_list)

# Values
# Getting all values
values = student.values()
print(values)

# Converting values to a list
value_list = list(values)
print(value_list)

# Items
# Getting all key-value pairs
items = student.items()
print(items)

# Converting items to a list
item_list = list(items)
print(item_list)

# get
# Getting the value for a key
name = student.get("name")
print(name)

# Getting the value for a non-existent key
country = student.get("country")
print(country)  # Output: None

# Getting the value for a non-existent key with a default value
country = student.get("country", "Unknown")
print(country)  # Output: Unknown

# pop
# Removing and returning a value
age = student.pop("grade")
print(age)
print(student)

# Removing a non-existent key with a default value
country = student.pop("country", "Unknown")
print(country)  # Output: Unknown

# update
student = {
    "name": "John",
    "age": 25,
    "city": "London"
}

# Updating with a dictionary
new_info = {
    "age": 26,
    "country": "United Kingdom"
}

student.update(new_info)
print(student)
# Output: {'name': 'John', 'age': 26, 'city': 'London', 'country': 'United Kingdom'}
