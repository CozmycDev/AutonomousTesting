from json import load, dump
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class FileFormatter:
    @staticmethod
    def _get_or_create_file(file_name: str) -> open:
        try:
            return open(file_name, "r")
        except FileNotFoundError as e:
            with open(file_name, "w") as file:
                pass
            return open(file_name)
        except Exception as e:
            logger.error(f"Error creating file {e}")
            raise

    @staticmethod
    def format_file(file_name: str, content: Optional[str] = None):
        if not content:
            logger.error("Content is required")
            raise ValueError("Content is required")
        
        try:
            with FileFormatter._get_or_create_file(file_name) as file:
                data = {"content": content}
                dump(data, file)
        except Exception as e:
            logger.error(f"Error saving to file: {e}")

    @staticmethod
    def format_file_from_json(file_name: str):
        try:
            with open(file_name, "r") as file:
                data = load(file)
                return data.get("content", None)
        except FileNotFoundError:
            logger.error(f"No JSON file found at {file_name}")
        except Exception as e:
            logger.error(f"Error loading from file: {e}")

    @staticmethod
    def format_file_to_json(file_name: str, content: Optional[str] = None) -> None:
        if not content:
            logger.error("Content is required")
            raise ValueError("Content is required")
        
        try:
            with open(file_name, "w") as file:
                data = {"content": content}
                dump(data, file)
        except Exception as e:
            logger.error(f"Error saving to JSON file: {e}")