from typing import Dict, Any
import json
from BaseFileSection import BaseFileSection  # Import from the relevant file


class File(BaseFileSection):
    def __init__(self, file_name: str, save_path: str, content: Dict[str, Any] = None):
        self.file_data = {"file_name": file_name, "save_path": save_path}
        super().__init__("File")
        self._data = {}

    @property
    def data(self) -> Dict[str, Any]:
        return self._data

    @data.setter
    def data(self, value: Dict[str, Any]):
        if not isinstance(value, dict):
            raise ValueError("Data must be a dictionary")
        if not self._validate_data(value):
            raise ValueError("Invalid JSON format")
        self._data = value

    @classmethod
    def load_from_file(cls, file_name: str) -> Dict[str, Any]:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                cls._load_data(data)
                return {k: v for k, v in data.get("content", {}).items() if v is not None}
        except Exception as e:
            print(f"Error loading from file: {e}")
            return {}

    @classmethod
    def _load_data(cls, data):
        if not isinstance(data, dict) or len(data.get("content", {}).items()) == 0:
            raise ValueError("Invalid JSON format")
        cls._data = {"content": data}

    @classmethod
    def validate_file_content(cls, file_name: str, expected_content: Dict[str, Any]) -> None:
        try:
            content = cls.load_from_file(file_name)
            if json.dumps(expected_content) != json.dumps(content):
                raise ValueError(f"Expected content is not a valid JSON format")
            self._data = {"content": expected_content}
        except Exception as e:
            print(f"Error validating file content: {e}")

    @classmethod
    def create_new_file(cls, save_path: str) -> "File":
        return cls(save_path, {"content": {}})

    @classmethod
    def get_data(cls, file_name: str) -> Dict[str, Any]:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                return data.get("content", {})
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
    def update_file_content(cls, file_name: str, new_content: Dict[str, Any]) -> None:
        cls._load_data({})
        with open(file_name, "w") as file:
            json.dump(new_content, file)

    @staticmethod
    def _validate_data(value: Dict[str, Any]) -> bool:
        return all(v is not None for v in value.values())

    @classmethod
    def check_file_validity(cls, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                if cls._validate_data(data.get("content", {})):
                    return True
        except Exception as e:
            print(f"Error checking file validity: {e}")
        return False