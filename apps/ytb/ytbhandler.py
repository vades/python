from pytube import YouTube
from pytube.exceptions import PytubeError, RegexMatchError, VideoUnavailable, MembersOnly, RecordingUnavailable, LiveStreamError
import moviepy.editor as mp
# from moviepy.editor import MoviePyError
from slugify import slugify


class YtbHandler:
    def __init__(self, config, video_id):
        self.config = config
        self.video_id = video_id
        self.video_url = config.ytb.video_url + video_id

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
                output_path=self.config.ytb.download_dir, filename=filename)
            return filename
        except PytubeError as e:
            # Handle general pytube exceptions
            print("A Pytube error occurred:", str(e))

    def video_to_audio(self, video_file):
        """
        Convert downloaded video to audio in MP3 format.

        Args:
            video (str): Path to the file.
        """
        try:
            downloaded_video = f'{self.config.ytb.download_dir}/{video_file}'
            video_clip = mp.VideoFileClip(downloaded_video)
            audio_clip = video_clip.audio
            audio_output = f'{self.config.mp3_output_dir}/{video_file[:-4]}.mp3'
            audio_clip.write_audiofile(audio_output)
            audio_clip.close()
        except Exception as e:
            # Exception handling code
            print("MoviePyError occurred:", str(e))
