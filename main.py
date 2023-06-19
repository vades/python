
# from libs.nestednamespace import NestedNamespace
from environments.config import config
from apps.ytb.ytbhandler import YtbHandler
""" config = {
    # load shared development variables
    **dotenv_values("environments/.env.shared"),
    **dotenv_values("environments/.env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
} """


def print_error_message(message):
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED}Error: {message}{RESET}")


# Example usage
error_message = "Something went wrong!"
print_error_message(error_message)

print('\n*********** Initializing video YouTube: ***********')
ytb = YtbHandler(config, 'Gtp6WkuoClM')
print('\n*********** Downloading video: ***********')
# downloaded_video = ytb.download_video()
downloaded_video = 'python-for-beginners-3-chat-gpt-Gtp6WkuoClM.mp4'
ytb.video_to_audio(downloaded_video)
""" config_dict = {
    'parent': {
        'child': {
            'grandchild': 'value'
        }
    },
    'normal_key': 'normal value',
}

config = NestedNamespace(config_dict) """

""" print(config)  # value
print(config.secret_key)  # normal value """
