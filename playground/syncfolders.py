from apps.sync.foldersynchronizer import FolderSynchronizer


# Example usage
source_folder = './_input/source/'
destination_folder = './_input/destination/'

synchronizer = FolderSynchronizer(source_folder, destination_folder)
synchronizer.synchronize_folders()
