TODO:
## YTB class

G:\My Drive\Shared\KB\Projects\Cheat Sheets
- [ ] Test multiple downloads
- [ ] Google Drive: https://developers.google.com/drive/api/quickstart/python
- [ ] Download from git and push to git: Sync on windows? or Linux?
- [ ] Research for python log module: https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module

C:\Users\vades\AppData\Local\Programs\Python\Python310\python.exe
C:\Dev\python
C:\Dev\python\_download\cheatsheets\gitpush.py

Create a cheat sheet that lists the most frequently used "Python date format" commands. Organize the cheat sheet as a markdown table with headers: format, short description, and example. To prevent the markdown table from breaking, remove any end of line characters in the rows. Additionally, provide a brief description of the table above it to provide context.


Construct a Python class named YtbHandler with two methods method called download_video and video_to_audio. The primary objective of the download_video method is to download video from youtube. Ensure that the method has a single parameter, video, representing the path to the file. The primary objective of the video_to_audio method is to convert downloaded video to audio mp3 format. Ensure that the method has a single parameter, video, representing the path to the file. To enhance code readability, include a comment within the function to document its purpose.


```python
from pytube import YouTube
from tqdm import tqdm

# URL of the video you want to download
video_url = "https://www.youtube.com/watch?v=video_id"

# Create a YouTube object
yt = YouTube(video_url)

# Select the first available video format (usually the highest quality)
video = yt.streams.first()

# Get the total file size in bytes
file_size = video.filesize

# Start the download
print("Downloading...")
progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)

def progress_callback(stream, chunk, bytes_remaining):
    # Calculate the percentage of downloaded bytes
    bytes_downloaded = file_size - bytes_remaining
    progress = bytes_downloaded / file_size * 100

    # Update the progress bar
    progress_bar.update(bytes_downloaded - progress_bar.n)

# Download the video with progress update
video.download(output_path='path/to/save', filename='video_file', on_progress_callback=progress_callback)

# Close the progress bar
progress_bar.close()

print("Download completed!")

```

```python
from pytube import YouTube
from pytube.exceptions import PytubeError, RegexMatchError, VideoUnavailable, \
    MembersOnly, RecordingUnavailable, LiveStreamError

try:
    # Code that may raise pytube exceptions
    video_url = "https://www.youtube.com/watch?v=VIDEO_ID"
    youtube = YouTube(video_url)

    # Access video details or download it
    video = youtube.streams.first()
    video.download()
except PytubeError as e:
    # Handle general pytube exceptions
    print("A Pytube error occurred:", str(e))
except RegexMatchError as e:
    # Handle regex match errors
    print("Regex match error:", str(e))
except VideoUnavailable as e:
    # Handle video unavailable errors
    print("Video is unavailable:", str(e))
except MembersOnly as e:
    # Handle members-only errors
    print("This video requires a membership:", str(e))
except RecordingUnavailable as e:
    # Handle recording unavailable errors
    print("Recording is unavailable for this video:", str(e))
except LiveStreamError as e:
    # Handle live stream errors
    print("This video is a live stream:", str(e))
except Exception as e:
    # Handle any other unexpected exceptions
    print("An unexpected error occurred:", str(e))

```


```python
import shutil
from git import Repo
import os


def change_permissions_recursive(path, mode):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in [os.path.join(root, d) for d in dirs]:
            os.chmod(dir, mode)
    for file in [os.path.join(root, f) for f in files]:
        os.chmod(file, mode)


def upload_directory_to_git(directory_path, repository_url, branch_name):
    # Clone the repository
    repo = Repo.clone_from(repository_url, "temp_repo")
    change_permissions_recursive('temp_repo', 0o777)
    # Change to the desired branch
    repo.git.checkout(branch_name)

    # Remove existing files in the repository directory
    existing_files = os.listdir(repo.working_tree_dir)
    for file_name in existing_files:
        file_path = os.path.join(repo.working_tree_dir, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            shutil.rmtree(file_path)

    # Copy files from the local directory to the repository directory
    files_to_upload = os.listdir(directory_path)
    for file_name in files_to_upload:
        file_path = os.path.join(directory_path, file_name)
        destination_path = os.path.join(repo.working_tree_dir, file_name)

        if os.path.isfile(file_path):
            shutil.copy2(file_path, destination_path)
        else:
            shutil.copytree(file_path, destination_path)

    # Commit and push changes to the branch
    repo.git.add("--all")
    repo.git.commit("-m", "Upload directory")
    repo.git.push("origin", branch_name)

    # Clean up temporary repository directory
    shutil.rmtree("temp_repo")


# Example usage
directory_path = "./_input/docs"
repository_url = "https://github.com/vades/cheatsheets"
branch_name = "develop"

upload_directory_to_git(directory_path, repository_url, branch_name)

```

```python
def print_error_message(message):
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED}Error: {message}{RESET}")

# Example usage
error_message = "Something went wrong!"
print_error_message(error_message)

```


Certainly! Here's an example of a Python script that runs another script after completing its execution and changing the current working directory:

```python
import os
import subprocess

def run_script(script_path):
    # Run the initial script
    subprocess.call(["python", script_path])

    # Change the current working directory to the desired folder
    target_folder = r"C:\path\to\folder"
    os.chdir(target_folder)

    # Run the second script
    subprocess.call(["python", "second_script.py"])

# Example usage
initial_script_path = r"C:\path\to\initial_script.py"
run_script(initial_script_path)
```

In this script, the `run_script()` function is defined to execute the initial script specified by its file path. After the initial script completes, it changes the current working directory to the desired folder using `os.chdir()`. Then, it runs the second script by calling `subprocess.call()` with the appropriate arguments.

To use this script, replace `C:\path\to\folder` with the actual path of the folder you want to change to, and `C:\path\to\initial_script.py` with the actual file path of the initial script you want to run.

Make sure that both Python scripts are located in accessible directories and have the necessary permissions to execute.

Feel free to modify the script according to your specific requirements, such as passing command-line arguments or handling any error conditions that may arise during script execution.










