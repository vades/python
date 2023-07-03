import datetime
from libs.logger import Logger
filename = "scheduled.txt"
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
text = f'{formatted_datetime} - The script ran \n'


# Logger.debug('This is message', True)
try:
    print(1 / 0)
except Exception:
    Logger.exception('New message', True)
# Open the file in write mode
# with open(filename, 'a') as file:
    # Write the text to the file
    # file.write(text)
