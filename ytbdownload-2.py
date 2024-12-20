import yt_dlp
import os
from slugify import slugify  # Requires `python-slugify` package


def get_download_directory():
    """Prompt user for a download directory and validate the path."""
    download_dir = input("Enter the download directory: ").strip()
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir


def get_video_urls_from_file():
    """Prompt user for a file name, read video URLs from the file, and validate the file's existence."""
    while True:
        file_name = input("Enter the file name containing the video URLs: ").strip()
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                urls = [line.strip() for line in file if line.strip()]
            if urls:
                return urls
            else:
                print("The file is empty. Please provide a file with valid video URLs.")
        else:
            print(f"Error: The file '{file_name}' does not exist. Please try again.")


def generate_filename(index, title):
    """Generate a filename as a slug with a leading index."""
    slug = slugify(title)
    return f"{slug}.mp4"
    #return f"{index:02d}-{slug}.mp4"


# Get download directory from user input
download_directory = get_download_directory()

# Get video URLs from the file provided by the user
video_urls = get_video_urls_from_file()

# Download each video with indexed filenames
with yt_dlp.YoutubeDL() as ydl:
    for index, video_url in enumerate(video_urls, start=1):
        try:
            print(f"Downloading video: {video_url}")

            # Extract video info to get the title
            info = ydl.extract_info(video_url, download=False)
            video_title = info.get('title', 'video')

            # Create indexed slugified filename
            output_template = os.path.join(download_directory, generate_filename(index, video_title))

            ydl_opts = {
                'outtmpl': output_template,
            }

            # Download the video with the current options
            with yt_dlp.YoutubeDL(ydl_opts) as ydl_with_opts:
                ydl_with_opts.download([video_url])

        except Exception as e:
            print(f"Failed to download video {video_url}: {e}")
