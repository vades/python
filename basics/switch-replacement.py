# In Python, there is no built-in `switch` statement like in some other programming languages. However,
# you can achieve similar functionality using other control flow statements.
# You can use an `if`/`elif` statement to achieve similar functionality:
day = 4
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

# Match
# Note that `match` is a relatively new feature in Python and is only available in Python 3.10 and later versions.
# It may not be widely adopted yet and may not be available in all Python environments.


def process_value(value):
    match value:
        case 0:
            print("The value is zero")
        case 1:
            print("The value is one")
        case str() as s:
            print(f"The value is a string: {s}")
        case list() as l if len(l) > 0:
            print(f"The value is a non-empty list: {l}")
        case _:
            print("The value is something else")


process_value(0)           # The value is zero
process_value(1)           # The value is one
process_value("hello")     # The value is a string: hello
process_value([])          # The value is something else
process_value([1, 2, 3])   # The value is a non-empty list: [1, 2, 3]
