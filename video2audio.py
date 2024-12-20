from moviepy.editor import VideoFileClip

# Load the video file
video = VideoFileClip("download/Perfekter Nebel zum fotografieren ｜ Landschaftsfotografie.mp4")

# Extract audio and save as mp3
audio = video.audio
audio.write_audiofile("download/audio.mp3")