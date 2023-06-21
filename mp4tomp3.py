import os
from apps.audio.audiohandler import AudioHandler
from config.config import config
from libs.commonutils import CommonUtils as utils


def mp4_to_mp3(video_file):

    video_name = os.path.basename(video_file)
    audio_file = f'{config.mp3_output_dir}/{video_name[:-4]}.mp3'
    print('\n*********** Initializing AudioHandler ***********')
    au = AudioHandler()
    print(f'\n*********** Converting {video_file} to mp3 ***********')
    au.video_to_audio(video_file, audio_file)
    print(f'\n*********** Done {audio_file} ***********')


# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    files = utils.list_files_with_extension(config.ytb.download_dir, ['mp4'])
    for video_file in files:
        mp4_to_mp3(video_file)
