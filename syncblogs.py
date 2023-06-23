from config.config import config
from apps.sync.foldersynchronizer import FolderSynchronizer
from apps.copy.copyhandler import CopyHandler


def sync_blogs():
    for blog in config.blogs:
        sync = FolderSynchronizer(
            blog['source_folder'], blog['destination_folder'])
        sync.synchronize_folders()


# TODO: Deprecated
""" def copy_blogs():
    for blog in config.blogs:
        copy = CopyHandler(blog['source_folder'],
                           blog['destination_folder'], blog['dirs_exist_ok'])
    copy.copy_folders() """


# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    sync_blogs()
    # copy_blogs()
