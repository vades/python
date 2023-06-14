import json


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
                config = json.load(file)
            return config
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON file: {file_path}", e.doc, e.pos) from e
