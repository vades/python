import datetime

filename = "scheduled.txt"
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
text = f'{formatted_datetime} - The script ran \n'

# Open the file in write mode
with open(filename, 'a') as file:
    # Write the text to the file
    file.write(text)
