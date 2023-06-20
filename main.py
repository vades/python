
from environments.config import config
from apps.ytb.main import ytb_video_to_audio

# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    ytb_video_to_audio(config)
