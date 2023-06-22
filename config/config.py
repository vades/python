import os
from dotenv import dotenv_values
from libs.nestednamespace import NestedNamespace

env_dict = {
    # load shared development variables
    **dotenv_values(".env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}
config_dict = {
    'app_name': 'Pythomat',
    'download_dir': './_download',
    'mp3_output_dir': './_output/mp3',
    'ytb': {
        'video_url': 'https://www.youtube.com/watch?v=',
        'download_dir': './_download/ytb',
    },
    'secret_key': env_dict['SECRET_KEY'],
    'blogs': [{
        'source_folder': r'G:/My Drive/Shared/KB/Blogs/Cheat Sheets',
        'destination_folder': r'_download/cheatsheets/docs',
        'dirs_exist_ok': True
    }],
    'gits': {
        'cheatsheets': {
            'repository_url': 'https://github.com/vades/cheatsheets',
            'branch_name': 'develop',
            'destination_folder': '_download/cheatsheets',
        },
    },
}
try:
    config = NestedNamespace(config_dict)
except Exception as e:
    print("An error occurred while creating config:", e)
