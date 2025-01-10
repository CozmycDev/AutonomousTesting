from json import load, dump
import os
from typing import Optional
import logging
import pathlib  # Import for Path class

logger = logging.getLogger(__name__)

class FileFormatter:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def _get_or_create_file(self) -> pathlib.Path:
        try:
            return pathlib.Path(self.file_name)
        except FileNotFoundError as e:
            pathlib.Path(self.file_name).touch()  # Touch to create file
            return pathlib.Path(self.file_name)
        except Exception as e:
            logger.error(f"Error creating file {e}")
            raise

    def format_file(self, content: Optional[str] = None):
        if not content:
            logger.error("Content is required")
            raise ValueError("Content is required")

        try:
            with self._get_or_create_file() as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logger.error(f"Error saving to file: {e}")

    def format_file_from_json(self):
        try:
            with open(str(self._get_or_create_file()), "r") as file:
                return load(file).get("content", None)
        except FileNotFoundError:
            logger.error(f"No JSON file found at {self.file_name}")
        except Exception as e:
            logger.error(f"Error loading from file: {e}")

    def format_file_to_json(self, content: Optional[str] = None) -> None:
        if not content:
            logger.error("Content is required")
            raise ValueError("Content is required")

        try:
            with self._get_or_create_file().open("w") as file:
                data = {"content": content}
                dump(data, str(file))
        except Exception as e:
            logger.error(f"Error saving to JSON file: {e}")