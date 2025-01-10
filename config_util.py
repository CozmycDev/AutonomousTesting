from typing import Dict, Any
import json
from BaseFileSection import BaseFileSection  # Import from the relevant file


class File(BaseFileSection):
    def __init__(self, file_name: str, save_path: str, content: str = None):
        super().__init__("File")
        self._file_name = file_name
        self.save_path = save_path
        self._data = {}

    @property
    def data(self) -> Dict[str, Any]:
        return {"content": {k: v for k, v in self._data.items() if v is not None}}

    @data.setter
    def data(self, value: Dict[str, Any]):
        if not isinstance(value, dict):
            raise ValueError("Data must be a dictionary")
        self._data = {k: v for k, v in value.items() if v is not None}

    def get_value(self) -> str:
        return self.data.get("content", "")

    @classmethod
    def load_from_file(cls, file_name: str):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                cls._data = {k: v for k, v in data.get("content", {}).items() if v is not None}
        except Exception as e:
            print(f"Error loading from file: {e}")

    def save_to_file(self):
        try:
            with open(self.save_path, "w") as file:
                json.dump({"content": self._data}, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def validate_file_content(file_name: str, content: str) -> None:
        File.load_from_file(file_name)
        if content != File.get_value():
            raise ValueError("File content has changed")

    @classmethod
    def create_new_file(cls, save_path: str):
        new_file = cls(save_path, "")
        return new_file

    @staticmethod
    def get_data(file_name: str) -> Dict[str, Any]:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                return {k: v for k, v in data.get("content", {}).items() if v is not None}
        except Exception as e:
            print(f"Error getting data from file: {e}")
            return {}

    @classmethod
    def get_file_value(cls, file_name: str) -> str:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                return data.get("content", "")
        except Exception as e:
            print(f"Error getting file value: {e}")
            return ""