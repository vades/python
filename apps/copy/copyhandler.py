import os
import shutil


class CopyHandler:
    def __init__(self, source_folder: str, destination_folder: str, dirs_exist_ok=False) -> None:
        self.source_folder = source_folder
        self.destination_folder = destination_folder
        self.dirs_exist_ok = dirs_exist_ok

    def copy_folders(self):
        try:
            # Check if the source folder exists
            if not os.path.exists(self.source_folder):
                raise FileNotFoundError("Source folder does not exist.")
            # Check if the destination folder exists
            if not os.path.exists(self.destination_folder):
                os.makedirs(self.destination_folder)

            shutil.copytree(self.source_folder,
                            self.destination_folder, dirs_exist_ok=self.dirs_exist_ok)
        except Exception as e:
            print("An error occurred while copying folders:", e)
