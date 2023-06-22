from git import Repo
from config.config import config
from apps.git.githandler import GitHandler


def clone_cheatsheets():

    repository_url = "https://github.com/vades/cheatsheets"
    branch_name = "develop"
    destination_folder = "_download/cheatsheets"
    print('\n*********** Initializing GitHandler ***********')
    git = GitHandler(repository_url, branch_name, destination_folder)
    print(f'\n*********** Cloning from git {repository_url} ***********')
    git.clone_repo_from_git()
    print(f'\n*********** Done ***********')


def upload_directory_to_git(branch_name):
    # Clone the repository
    # repo = Repo.clone_from(repository_url, "temp_repo")

    # Initialize the repository object
    repo = Repo()

    # Check if there are changes to commit
    # if repo.is_dirty():
    repo.git.add("--all")
    repo.git.commit("-m", "Upload directory")
    repo.git.push("origin", branch_name)
   # else:
    # print("No changes to commit.")


# Example usage
""" directory_path = "./_input/docs"
repository_url = "https://github.com/vades/cheatsheets"
branch_name = "develop"

upload_directory_to_git(branch_name) """

# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    clone_cheatsheets()
