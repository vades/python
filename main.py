
from config.config import config
from ytbtoaudio import ytb_video_to_audio
from apps.audio.audiohandler import AudioHandler
from libs.commonutils import CommonUtils as utils

# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    video_name = 'python-for-beginners-3-chat-bot-Gtp6WkuoClM.mp4'
    video_file = f'{config.ytb.download_dir}/{video_name}'
    audio_file = f'{config.mp3_output_dir}/{video_name[:-4]}.mp3'
    au = AudioHandler()
    au.video_to_audio(video_file, audio_file)
    """ files = utils.list_files_with_extension('config', ['py'])
    for file in files:
        print(file) """
    # ytb_video_to_audio(config)
