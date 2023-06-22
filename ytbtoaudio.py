from config.config import config
from apps.ytb.ytbhandler import YtbHandler

video_ids = ['Gtp6WkuoClM', '2cvKpW0E74Y']


def ytb_video_to_audio(video_id):
    print('\n*********** Initializing video YouTube ***********')
    ytb = YtbHandler(video_id, config.ytb.video_url, config.ytb.download_dir)
    print(f'\n*********** Downloading video {video_id} ***********')
    downloaded_video = ytb.download_video()
    print(f'\n*********** Downloaded {downloaded_video} ***********')


# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    for video_id in video_ids:
        ytb_video_to_audio(video_id)
