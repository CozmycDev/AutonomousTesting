from json import load, dump
import os
from typing import Optional
import logging
import pathlib  # Import for Path class

class FileFormatter:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self._file_path = pathlib.Path(self.file_name)

    def format_file(self, content: Optional[str] = None) -> None:
        if not content:
            raise ValueError("Content is required")
        
        try:
            with self._file_path.open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to file: {e}")

    def format_file_from_json(self) -> Optional[str]:
        try:
            with self._file_path.open("r") as file:
                return load(str(file)).get("content", None)
        except FileNotFoundError:
            logging.error(f"No JSON file found at {self.file_name}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    def format_file_to_json(self, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with self._file_path.open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")

    def _validate_content(self, content: Optional[str]) -> None:
        if not content:
            raise ValueError("Content is required")

    @classmethod
    def create_file(cls, file_name: str) -> pathlib.Path:
        return cls(file_name).file_path

    @classmethod
    def exists_file(cls, file_name: str) -> bool:
        return cls.create_file(file_name).exists()

    @classmethod
    def get_content(cls, file_name: str) -> Optional[str]:
        try:
            with cls.create_file(file_name).open("r") as file:
                data = load(str(file))
                if 'content' in data:
                    return data['content']
                else:
                    raise KeyError('Content key not found')
        except FileNotFoundError:
            logging.error(f"No JSON file found at {file_name}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    @classmethod
    def update_content(cls, file_name: str, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with cls.create_file(file_name).open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")

    @classmethod
    def remove_file(cls, file_name: str) -> None:
        if cls.exists_file(file_name):
            cls.create_file(file_name).touch()
            os.remove(str(cls.create_file(file_name)))

    @classmethod
    def format_file_to_json_with_error_handling(cls, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with self._file_path.open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")

    @classmethod
    def load_file_from_json(cls, file_name: str) -> Optional[str]:
        try:
            with cls.create_file(file_name).open("r") as file:
                data = load(str(file))
                if 'content' in data:
                    return data['content']
                else:
                    raise KeyError('Content key not found')
        except FileNotFoundError:
            logging.error(f"No JSON file found at {file_name}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    @classmethod
    def save_file_to_json(cls, file_name: str, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with cls.create_file(file_name).open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")

    @classmethod
    def delete_file(cls, file_name: str) -> None:
        if cls.exists_file(file_name):
            cls.create_file(file_name).touch()
            os.remove(str(cls.create_file(file_name)))

    @classmethod
    def exists_path(cls, path: str) -> bool:
        return cls.create_file(path).exists()

    @classmethod
    def get_directory_content(cls, dir_name: str) -> Optional[str]:
        try:
            with cls.create_file(dir_name).open("r") as file:
                data = load(str(file))
                if 'content' in data:
                    return data['content']
                else:
                    raise KeyError('Content key not found')
        except FileNotFoundError:
            logging.error(f"No JSON file found at {dir_name}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    @classmethod
    def update_directory_content(cls, dir_name: str, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with cls.create_file(dir_name).open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")

    @classmethod
    def delete_directory(cls, dir_name: str) -> None:
        if cls.exists_path(dir_name):
            cls.create_file(dir_name).touch()
            import os
            os.rmdir(dir_name)

    @classmethod
    def get_parent_directory_content(cls, parent_dir: str) -> Optional[str]:
        try:
            with cls.create_file(parent_dir).open("r") as file:
                data = load(str(file))
                if 'content' in data:
                    return data['content']
                else:
                    raise KeyError('Content key not found')
        except FileNotFoundError:
            logging.error(f"No JSON file found at {parent_dir}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    @classmethod
    def update_parent_directory_content(cls, parent_dir: str, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with cls.create_file(parent_dir).open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")

    @classmethod
    def delete_parent_directory(cls, parent_dir: str) -> None:
        if cls.exists_path(parent_dir):
            cls.create_file(parent_dir).touch()
            import os
            os.rmdir(parent_dir)

    @classmethod
    def get_subdirectory_content(cls, sub_dir: str) -> Optional[str]:
        try:
            with cls.create_file(sub_dir).open("r") as file:
                data = load(str(file))
                if 'content' in data:
                    return data['content']
                else:
                    raise KeyError('Content key not found')
        except FileNotFoundError:
            logging.error(f"No JSON file found at {sub_dir}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    @classmethod
    def update_subdirectory_content(cls, sub_dir: str, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with cls.create_file(sub_dir).open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")

    @classmethod
    def delete_subdirectory(cls, sub_dir: str) -> None:
        if cls.exists_path(sub_dir):
            cls.create_file(sub_dir).touch()
            import os
            os.rmdir(sub_dir)

    @classmethod
    def get_files_in_directory(cls, dir_name: str) -> list:
        try:
            with cls.create_file(dir_name).open("r") as file:
                data = load(str(file))
                if 'files' in data:
                    return data['files']
                else:
                    raise KeyError('Files key not found')
        except FileNotFoundError:
            logging.error(f"No JSON file found at {dir_name}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    @classmethod
    def delete_files_in_directory(cls, dir_name: str) -> None:
        if cls.exists_path(dir_name):
            cls.create_file(dir_name).touch()
            import os
            files = [f for f in os.listdir(dir_name)]
            for file in files:
                try:
                    os.remove(f"{dir_name}/{file}")
                except Exception as e:
                    logging.error(f"Error deleting {e}")

    @classmethod
    def create_new_file(cls, new_file: str) -> None:
        try:
            with cls.create_file(new_file).open("w") as file:
                pass
        except Exception as e:
            logging.error(f"Error creating {e}")

    @classmethod
    def update_new_file(cls, new_file: str, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with cls.create_file(new_file).open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error updating {e}")

    @classmethod
    def delete_new_file(cls, new_file: str) -> None:
        if cls.exists_path(new_file):
            cls.create_file(new_file).touch()
            import os
            os.remove(str(cls.create_file(new_file)))