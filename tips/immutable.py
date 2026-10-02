# Immutable variables:
age = 30
name = "John"
coordinates = (0, 0)

# Mutable variables:
my_list = [1, 2, 3, 4]
my_dict = {"name": "John", "age": 30}
my_set = {1, 2, 3, 4}

# For example, you can use an immutable variable as a dictionary key
my_dict = {(0, 0): "origin", (1, 0): "east", (0, 1): "north", (-1, 0): "west", (0, -1): "south"}

# But you cannot use a mutable variable as a dictionary key:
my_dict = {[1, 2, 3]: "my list"}  # TypeError: unhashable type: 'list'

print(my_dict)
