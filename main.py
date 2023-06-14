import os
from dotenv import dotenv_values

config = {
    # load shared development variables
    **dotenv_values("environments/.env.shared"),
    **dotenv_values("environments/.env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}


print(config['APP_NAME'])
