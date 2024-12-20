import os
from moviepy.editor import VideoFileClip
# TODO: Read from nested directories

def read_directory(prompt_message):
    """
    Prompts the user for a directory path and validates it.
    """
    while True:
        path = input(prompt_message)
        if os.path.isdir(path):
            return path
        else:
            print("Invalid directory. Please try again.")


def get_video_list(source_dir):
    """
    Creates a list of video files (MP4) from the given directory.
    """
    return [file for file in os.listdir(source_dir) if file.endswith('.mp4')]


def create_directory_if_not_exists(directory):
    """
    Creates the target directory if it does not exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def convert_to_mp3(source_path, target_path):
    """
    Converts a video file to MP3 and saves it to the target path.
    """
    try:
        with VideoFileClip(source_path) as video:
            audio = video.audio
            if audio:  # Ensure the video has an audio track
                audio.write_audiofile(target_path)
    except Exception as e:
        print(f"Error converting {source_path}: {e}")


def loop_through_videos(video_list, source_dir, target_dir):
    """
    Loops through the video list, converting each to MP3.
    """
    for video_file in video_list:
        source_path = os.path.join(source_dir, video_file)
        target_path = os.path.join(target_dir, os.path.splitext(video_file)[0] + '.mp3')
        print(f"Converting {video_file}...")
        convert_to_mp3(source_path, target_path)


def main():
    """
    Main function to execute the program.
    """
    source_dir = read_directory("Enter the path to the source directory with videos: ")
    target_dir = input("Enter the path to the target directory for audio files: ")

    create_directory_if_not_exists(target_dir)
    video_list = get_video_list(source_dir)

    if video_list:
        loop_through_videos(video_list, source_dir, target_dir)
        print("Conversion complete.")
    else:
        print("No MP4 videos found in the source directory.")


if __name__ == "__main__":
    main()
