# YTB - Convert Video to Audio Guide
This guide helps you download YouTube Music playlists, save the videos, and convert them to audio files.

## 1. Download a Playlist
To create a list of video URLs from a YouTube Music playlist:
1. Run the Script:  
   ```bash
   python playlist.py
   ```
   
2. Enter the YouTube Music Playlist URL when prompted (e.g., `https://music.youtube.com/playlist?list=YOUR_PLAYLIST_ID`).

3. Specify the Directory where you want to save the output file (e.g., `playlists`).

4. Enter the Output File Name (e.g., `my_playlist.txt`).



## 2. Download Videos from the Playlist

To download videos based on the saved playlist file:

1. Run the Script:  
   ```bash
   python ytbdownload-2.py
   ```

2. Enter the Download Directory (e.g., `downloads/music`).

3. Specify the File Containing the Video URLs (e.g., `playlists/my_playlist.txt`).



## 3. Convert Videos to Audio

To convert downloaded videos to audio files:

1. Run the Script:  
   ```bash
   python v2a.py
   ```

2. Enter the Path to the Source Directory where the videos are stored (e.g., `downloads/music`).

3. Enter the Path to the Target Directory where the audio files should be saved (e.g., `audio/music/artist/album-name`).



## 4. Known Issues

### Error Downloading Videos

If you encounter errors when downloading videos, update the `yt-dlp` library by running:

```bash
pip install -U yt-dlp
```



### Tips

- Ensure you have `pytube` and `yt-dlp` installed by running:  
  ```bash
  pip install pytube yt-dlp
  ```

- Keep your directory structure organized for easier management of playlists, downloads, and converted audio files.

