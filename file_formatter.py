from json import load, dump
import os
from typing import Optional

class FileFormatter:
    @staticmethod
    def _get_or_create_file(file_name: str):
        try:
            return open(file_name, "r")
        except FileNotFoundError:
            with open(file_name, "w") as file:
                pass
            return open(file_name)

    @staticmethod
    def format_file(file_name: str, content: Optional[str] = None):
        if not content:
            raise ValueError("Content is required")
        
        try:
            with FileFormatter._get_or_create_file(file_name) as file:
                data = {"content": content}
                dump(data, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def format_file_from_json(file_name: str):
        try:
            with open(file_name, "r") as file:
                data = load(file)
        except FileNotFoundError:
            print(f"No JSON file found at {file_name}")
        except Exception as e:
            print(f"Error loading from file: {e}")

        return data.get("content", None)