from json import load, dump
import os
from typing import Optional
import logging
import pathlib  # Import for Path class

class FileFormatter:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def _get_or_create_file(self) -> pathlib.Path:
        try:
            return pathlib.Path(self.file_name)
        except FileNotFoundError as e:
            self._create_file_if_not_exists()
            return pathlib.Path(self.file_name)
        except Exception as e:
            logging.error(f"Error creating file {e}")
            raise

    def _create_file_if_not_exists(self):
        if not os.path.exists(str(pathlib.Path(self.file_name))):
            pathlib.Path(self.file_name).touch()

    def format_file(self, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with self._get_or_create_file().open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to file: {e}")

    def _validate_content(self, content: Optional[str]) -> None:
        if not content:
            raise ValueError("Content is required")

    def format_file_from_json(self) -> Optional[str]:
        try:
            with self._get_or_create_file().open("r") as file:
                return load(str(file)).get("content", None)
        except FileNotFoundError:
            logging.error(f"No JSON file found at {self.file_name}")
        except Exception as e:
            logging.error(f"Error loading from file: {e}")

    def format_file_to_json(self, content: Optional[str] = None) -> None:
        self._validate_content(content)
        try:
            with self._get_or_create_file().open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")