from typing import Dict, Any
import json
from BaseFileSection import BaseFileSection  # Import from the relevant file


class File(BaseFileSection):
    def __init__(self, file_name: str, save_path: str, content: str = None):
        self._file_name = file_name
        self.save_path = save_path
        if content:
            super().__init__("File", {"content": content})
        else:
            super().__init__("File")

    @property
    def data(self) -> Dict[str, Any]:
        return self._data or {}

    @data.setter
    def data(self, value: Dict[str, Any]):
        if not isinstance(value, dict):
            raise ValueError("Data must be a dictionary")
        self._data = {"content": value.get("content", "")}

    def get_value(self) -> str:
        return self.data["content"]

    def save_to_file(self):
        try:
            with open(self.save_path, "w") as file:
                json.dump(self.data, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def _load_from_file(file_name: str) -> None:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                File._data = {"content": data["content"]}
        except Exception as e:
            print(f"Error loading from file: {e}")

    def save_to_json(self) -> str:
        return json.dumps(self.data)

 #