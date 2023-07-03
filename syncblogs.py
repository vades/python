from config.config import config
from apps.sync.foldersynchronizer import FolderSynchronizer
from libs.logger import Logger


def sync_blogs():
    for blog in config.blogs:
        sync = FolderSynchronizer(
            blog['source_folder'], blog['destination_folder'])
        Logger.debug(
            f"Synchronizing: {blog['source_folder']}  {blog['destination_folder']}", True)
        sync.synchronize_folders()


# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    sync_blogs()
