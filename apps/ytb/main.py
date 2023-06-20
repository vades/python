from apps.ytb.ytbhandler import YtbHandler


def ytb_video_to_audio(config):
    print('\n*********** Initializing video YouTube ***********')
    ytb = YtbHandler(config, 'Gtp6WkuoClM')
    print('\n*********** Downloading video ***********')
    downloaded_video = ytb.download_video()
    # downloaded_video = 'python-for-beginners-3-chat-bot-Gtp6WkuoClM.mp4'
    print('\n*********** Converting video to audio ***********')
    ytb.video_to_audio(downloaded_video)
