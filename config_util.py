from typing import Dict, Any
import json
from BaseFileSection import BaseFileSection  # Import from the relevant file


class File(BaseFileSection):
    def __init__(self, file_name: str, save_path: str, content: str = None):
        self._file_data = {"file_name": file_name, "save_path": save_path}
        super().__init__("File")
        self._data = {}
        if content:
            self.data = content

    @property
    def data(self) -> Dict[str, Any]:
        return {**self._data, **{"content": {k: v for k, v in self._data.items() if v is not None}}}

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
                cls._file_data["data"] = {k: v for k, v in data.get("content", {}).items() if v is not None}
        except Exception as e:
            print(f"Error loading from file: {e}")

    def save_to_file(self):
        try:
            with open(self.save_path, "w") as file:
                json.dump({**self._file_data, **{"content": self._data}}, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    @classmethod
    def validate_file_content(cls, file_name: str, content: str) -> None:
        cls.load_from_file(file_name)
        if content != cls.get_value():
            raise ValueError("File content has changed")

    @classmethod
    def create_new_file(cls, save_path: str):
        new_file = cls(save_path, {})
        return new_file

    @classmethod
    def get_data(cls, file_name: str) -> Dict[str, Any]:
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

    @classmethod
    def update_file_content(cls, file_name: str, content: str) -> None:
        try:
            with open(file_name, "w") as file:
                json.dump({"content": content}, file)
        except Exception as e:
            print(f"Error updating file content: {e}")