import os
import shutil
from git import Repo


class GitHandler:
    def __init__(self, repository_url: str, branch_name: str, destination_folder: str) -> None:
        self.repository_url = repository_url
        self.branch_name = branch_name
        self.destination_folder = destination_folder

    def clone_repo_from_git(self):
        try:
            # Check if the destination folder exists
            if not os.path.exists(self.destination_folder):
                os.makedirs(self.destination_folder)
                # Clone the repository
                repo = Repo.clone_from(self.repository_url,
                                       self.destination_folder)
                # Change to the desired branch
                repo.git.checkout(self.branch_name)
        except Exception as e:
            print("An error occurred while cloning from git:", e)
