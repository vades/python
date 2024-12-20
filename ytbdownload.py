import yt_dlp
# TODO: Accept target directory from prompt
# TODO: Create video file name as slug starting with array index: 01-video-name-as-slug.mp4
# Set download options with a custom directory
ydl_opts = {
    'outtmpl': 'download/%(title)s.%(ext)s'  # Replace with your desired path
}

# Prompt the user for comma-separated video IDs
video_urls = input("Enter the YouTube video URLs (comma-separated): ").split(',')

# Trim whitespace from each video ID and process each one
video_urls = [video_id.strip() for video_id in video_urls]

# Download each video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for video_url in video_urls:
        try:
            print(f"Downloading video: {video_url}")
            ydl.download([video_url])
        except Exception as e:
            print(f"Failed to download video {video_url}: {e}")
