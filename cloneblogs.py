from git import Repo
from config.config import config
from apps.git.githandler import GitHandler


def clone_cheatsheets():

    print('\n*********** Initializing GitHandler ***********')
    git = GitHandler(config.git.cheatsheets.repository_url,
                     config.git.cheatsheets.branch_name, config.git.cheatsheets.destination_folder)
    print(
        f'\n*********** Cloning from git {config.git.cheatsheets.repository_url} ***********')
    git.clone_repo_from_git()
    print(f'\n*********** Done ***********')


# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.
if __name__ == "__main__":
    clone_cheatsheets()
