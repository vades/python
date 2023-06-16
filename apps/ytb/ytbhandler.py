from pytube import YouTube
import moviepy.editor as mp
from slugify import slugify


class YtbHandler:
    def __init__(self, config, video_id):
        self.cfg = config
        self.video_id = video_id
        self.video_url = config['YTB_VIDEO_URL'] + video_id

    def download_video(self):
        """
        Download video from YouTube.

        Args:
            video (str): Path to the file.
        """
        ytb = YouTube(self.video_url)
        video_slug = slugify(ytb.title, max_length=32)
        filename = f'{video_slug}-{self.video_id}.mp4'
        video_stream = ytb.streams.get_highest_resolution()
        video_stream.download(
            output_path=self.cfg['YTB_DOWNLOAD_DIR'], filename=filename)

        return filename

    def video_to_audio(self, video_file):
        """
        Convert downloaded video to audio in MP3 format.

        Args:
            video (str): Path to the file.
        """
        downloaded_video = self.cfg['YTB_DOWNLOAD_DIR'] + '/' + video_file
        video_clip = mp.VideoFileClip(downloaded_video)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(
            f"{self.cfg['MP3_OUTPUT_DIR']}/{video_file[:-4]}.mp3")
        audio_clip.close()
