import os
from dotenv import dotenv_values
from apps.ytb.ytbhandler import YtbHandler
config = {
    # load shared development variables
    **dotenv_values("environments/.env.shared"),
    **dotenv_values("environments/.env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

ytb = YtbHandler(config, 'Gtp6WkuoClM')
downloaded_video = ytb.download_video()
ytb.video_to_audio(downloaded_video)
print(config['APP_DOWNLOAD_DIR'])
