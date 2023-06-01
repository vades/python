from pytube import YouTube
import moviepy.editor as mp


class YtbHandler:
    def download_video(self, video):
        """
        Download video from YouTube.

        Args:
            video (str): Path to the file.
        """
        yt = YouTube(video)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()

    def video_to_audio(self, video):
        """
        Convert downloaded video to audio in MP3 format.

        Args:
            video (str): Path to the file.
        """
        video_clip = mp.VideoFileClip(video)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(f"{video[:-4]}.mp3")
        audio_clip.close()
        video_clip.close()
