from pytube import YouTube
import moviepy.editor as mp
from slugify import slugify


class YtbHandler:
    def __init__(self, video_id):
        self.video_id = video_id
        self.video_url = 'https://www.youtube.com/watch?v=' + video_id

    def download_video(self):
        """
        Download video from YouTube.

        Args:
            video (str): Path to the file.
        """
        ytb = YouTube(self.video_url)
        # video_slug = slugify(ytb.title)
        filename = self.video_id + '.mp4'
        video_stream = ytb.streams.get_highest_resolution()
        video_stream.download(output_path="./_download", filename=filename)

        return filename

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
