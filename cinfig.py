import yaml
import os


class Config:
    def __init__(self):
        self.config_data = None

    def load_config(self, filename):
        """
        Function 1: Loads the YAML file from the config directory.
        """
        try:
            config_dir = os.path.join(os.path.dirname(__file__), 'config')
            config_path = os.path.join(config_dir, filename)

            with open(config_path, 'r') as file:
                self.config_data = yaml.safe_load(file)
            print(f"Configuration loaded successfully from {filename}")
        except FileNotFoundError:
            print(f"Error: Configuration file '{filename}' not found in the config directory.")
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_config(self):
        """
        Function 2: Displays the loaded YAML file as dictionaries.
        """
        try:
            if self.config_data is None:
                raise ValueError("No configuration data loaded. Please load a configuration file first.")

            print("Loaded Configuration:")
            self._display_dict(self.config_data)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _display_dict(self, data, indent=0):
        """
        Helper function to recursively display nested dictionaries.
        """
        for key, value in data.items():
            print("  " * indent + f"{key}:")
            if isinstance(value, dict):
                self._display_dict(value, indent + 1)
            else:
                print("  " * (indent + 1) + f"{value}")


# Example usage:
if __name__ == "__main__":
    config = Config()
    config.load_config("config.yaml")
    config.display_config()