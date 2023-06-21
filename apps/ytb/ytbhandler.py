from pytube import YouTube
from pytube.exceptions import PytubeError
import moviepy.editor as mp
from slugify import slugify


class YtbHandler:
    def __init__(self, video_id, video_url, download_dir):
        self.video_id = video_id
        self.video_url = video_url + video_id
        self.download_dir = download_dir

    def download_video(self):
        """
        Download video from YouTube.

        Args:
            video (str): Path to the file.
        """

        try:
            ytb = YouTube(self.video_url)
            video_slug = slugify(ytb.title, max_length=32)
            filename = f'{video_slug}-{self.video_id}.mp4'
            video_stream = ytb.streams.get_highest_resolution()
            video_stream.download(
                output_path=self.download_dir, filename=filename)
            return filename
        except PytubeError as e:
            # Handle general pytube exceptions
            print("A Pytube error occurred:", str(e))
