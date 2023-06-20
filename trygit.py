import shutil
from git import Repo
import os


def change_permissions_recursive(path, mode):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in [os.path.join(root, d) for d in dirs]:
            os.chmod(dir, mode)
    for file in [os.path.join(root, f) for f in files]:
        os.chmod(file, mode)


def upload_directory_to_git(directory_path, repository_url, branch_name):
    # Clone the repository
    repo = Repo.clone_from(repository_url, "temp_repo")
    change_permissions_recursive('temp_repo', 0o777)
    # Change to the desired branch
    repo.git.checkout(branch_name)

    # Remove existing files in the repository directory
    existing_files = os.listdir(repo.working_tree_dir)
    for file_name in existing_files:
        file_path = os.path.join(repo.working_tree_dir, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            shutil.rmtree(file_path)

    # Copy files from the local directory to the repository directory
    files_to_upload = os.listdir(directory_path)
    for file_name in files_to_upload:
        file_path = os.path.join(directory_path, file_name)
        destination_path = os.path.join(repo.working_tree_dir, file_name)

        if os.path.isfile(file_path):
            shutil.copy2(file_path, destination_path)
        else:
            shutil.copytree(file_path, destination_path)

    # Commit and push changes to the branch
    repo.git.add("--all")
    repo.git.commit("-m", "Upload directory")
    repo.git.push("origin", branch_name)

    # Clean up temporary repository directory
    shutil.rmtree("temp_repo")


# Example usage
directory_path = "./_input/docs"
repository_url = "https://github.com/vades/cheatsheets"
branch_name = "develop"

upload_directory_to_git(directory_path, repository_url, branch_name)
