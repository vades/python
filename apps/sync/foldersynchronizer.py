import os
import filecmp
import shutil


class FolderSynchronizer:
    def __init__(self, source_folder: str, destination_folder: str, delete_files=False):
        self.source_folder = source_folder
        self.destination_folder = destination_folder
        self.delete_files = delete_files

    def synchronize_folders(self):
        """
        Synchronizes the folders between source_folder and destination_folder.
        Recursively synchronizes files, subfolders, and deletes missing files.
        """
        try:
            self.synchronize_files()
            if (self.delete_files):
                self.delete_missing_files()
            self.synchronize_subfolders()
        except Exception as e:
            print("An error occurred during folder synchronization:", e)

    def synchronize_files(self):
        """
        Synchronizes files between source_folder and destination_folder.
        Copies files from source_folder to destination_folder if they don't exist or are different.
        """
        source_contents = os.listdir(self.source_folder)

        for item in source_contents:
            source_item = os.path.join(self.source_folder, item)
            destination_item = os.path.join(self.destination_folder, item)

            if os.path.isfile(source_item):
                try:
                    if not os.path.exists(destination_item) or not filecmp.cmp(source_item, destination_item, shallow=False):
                        self.copy_file(source_item)
                except Exception as e:
                    print("An error occurred while synchronizing file:", source_item)
                    print("Error details:", e)

    def synchronize_subfolders(self):
        """
        Recursively synchronizes subfolders between source_folder and destination_folder.
        """
        source_contents = os.listdir(self.source_folder)

        for item in source_contents:
            source_item = os.path.join(self.source_folder, item)
            destination_item = os.path.join(self.destination_folder, item)

            if os.path.isdir(source_item):
                try:
                    if not os.path.exists(destination_item):
                        self.create_directory(destination_item)
                    subfolder_synchronizer = FolderSynchronizer(
                        source_item, destination_item)
                    subfolder_synchronizer.synchronize_folders()
                except Exception as e:
                    print(
                        "An error occurred while synchronizing subfolder:", source_item)
                    print("Error details:", e)

    def delete_missing_files(self):
        """
        Deletes files in destination_folder that are missing in source_folder.
        """
        destination_contents = os.listdir(self.destination_folder)

        for item in destination_contents:
            destination_item = os.path.join(self.destination_folder, item)
            source_item = os.path.join(self.source_folder, item)

            if os.path.isfile(destination_item) and not os.path.exists(source_item):
                try:
                    self.delete_file(destination_item)
                except Exception as e:
                    print("An error occurred while deleting file:",
                          destination_item)
                    print("Error details:", e)

    def copy_file(self, source):
        """
        Copies a file from source to destination_folder.
        """
        try:
            shutil.copy2(source, self.destination_folder)
            print(f"Copied file: {source}")
        except Exception as e:
            print("An error occurred while copying file:", source)
            print("Error details:", e)

    def create_directory(directory):
        """
        Creates a directory if it doesn't exist.
        """
        try:
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        except Exception as e:
            print("An error occurred while creating directory:", directory)
            print("Error details:", e)

    def delete_file(self, file):
        """
        Deletes a file.
        """
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except Exception as e:
            print("An error occurred while deleting file:", file)
            print("Error details:", e)
