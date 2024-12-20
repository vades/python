import os
from pytube import Playlist

# Get playlist URL from user input
playlist_url = input("Enter the YouTube Music playlist URL: ")

# Initialize the playlist
playlist = Playlist(playlist_url)

# Print the number of videos
print(f'Number of videos in playlist: {len(playlist.video_urls)}')

# Get the output directory from the user
output_dir = input("Enter the directory where the output file should be saved (e.g., playlists): ")

# Ensure the directory exists; create it if it doesn't
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' was created.")

# Get the output filename from the user
output_file = input("Enter the name of the output file (e.g., my_playlist.txt): ")

# Full path for the output file
output_path = os.path.join(output_dir, output_file)

# Save the links to the specified txt file
with open(output_path, 'w') as file:
    for video_url in playlist.video_urls:
        file.write(video_url + '\n')

print(f'Playlist links have been saved to {output_path}')
