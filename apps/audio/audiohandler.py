import moviepy.editor as mp


class AudioHandler:
    def __init__(self) -> None:
        pass

    def video_to_audio(self, video_file, audio_file):
        """
        Convert downloaded video to audio in MP3 format.

        Args:
            video (str): Path to the file.
        """
        try:
            video_clip = mp.VideoFileClip(video_file)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(audio_file)
            audio_clip.close()
        except Exception as e:
            # Exception handling code
            print("MoviePyError occurred:", str(e))
