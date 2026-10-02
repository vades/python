import datetime
import time
""" Print current date in format YYYY-MM-DD """
print('\nPrint current date in format YYYY-MM-DD')

current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y-%m-%d")
print(current_date)

""" create a date object for January 1, 2022 """
print('\ncreate a date object for January 1, 2022')

d = datetime.date(2022, 1, 1)

# format the date as a string
s = d.strftime("%B %d, %Y")

# output the formatted string
print(s)   # January 01, 2022

""" Calculating the difference between two dates """
print('\nCalculating the difference between two dates')

# create two date objects
d1 = datetime.date(2022, 1, 1)
d2 = datetime.date(2022, 5, 15)

# calculate the difference between the dates
delta = d2 - d1

# output the difference in days
print(delta.days)   # 134

""" Adding or subtracting days from a date """
print('\nAdding or subtracting days from a date')

# create a date object for January 1, 2022
d = datetime.date(2022, 1, 1)

# add 30 days to the date
d = d + datetime.timedelta(days=30)

# output the new date
print(d)   # 2022-01-31

""" Parsing a date from a string """
print('\nParsing a date from a string')

# parse a date from a string
d = datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date()

# output the date
print(d)   # 2022-01-01

""" Converting a timestamp to a date """
print('\nConverting a timestamp to a date')

# create a timestamp for January 1, 2022 at 12:00:00 AM
timestamp = 1640995200

# convert the timestamp to a datetime object
dt = datetime.datetime.fromtimestamp(timestamp)

# extract the date from the datetime object
d = dt.date()

# output the date
print(d)   # 2022-01-01

""" Generating a sequence of dates """
print('\nGenerating a sequence of dates')
# get today's date
today = datetime.date.today()

# generate a sequence of dates for the next 7 days
for i in range(7):
    d = today + datetime.timedelta(days=i)
    print(d)

""" UNIX timestamp using time module """
print('\nUNIX timestamp using time module')

unix_timestamp = int(time.time())
print(unix_timestamp)
