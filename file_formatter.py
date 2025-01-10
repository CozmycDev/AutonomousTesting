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
                return load(str(file)).get("content", None)
        except FileNotFoundError:
            logging.error(f"No JSON file found at {file_name}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    @classmethod
    def update_content(cls, file_name: str, content: Optional[str] = None) -> None:
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