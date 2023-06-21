import json
import os


class CommonUtils:
    @staticmethod
    def read_json(file_path):
        """
        Extracts data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: A dictionary containing the data from json file.

        Raises:
            FileNotFoundError: If the file specified by `file_path` does not exist.
            JSONDecodeError: If the JSON file is not valid and cannot be decoded.

        Example:
            config_data = CommonUtils.read_config('/path/to/yourjson.json')
        """
        try:
            with open(file_path) as file:
                data = json.load(file)
            return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON file: {file_path}", e.doc, e.pos) from e

    def list_files_with_extension(directory, allowed_extensions):
        """
        Lists all files with a specific extension from a defined directory.

        Args:
            directory (str): The directory to search for files.
            allowed_extensions (list): A list of allowed file extensions.

        Returns:
            list: A list of file paths matching the specified extensions.

        Example:
            directory = '/path/to/directory'
            allowed_extensions = ['.txt', '.csv']

            matching_files = list_files_with_extension(directory, allowed_extensions)
            print(matching_files)
        """
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in allowed_extensions):
                    file_path = os.path.join(root, file)
                    file_list.append(file_path.replace('\\', '/'))
        return file_list
