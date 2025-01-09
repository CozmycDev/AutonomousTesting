from abc import ABC, abstractmethod
import json
from typing import Dict, Any

class FileSection(ABC):
    def __init__(self, name: str, data: Dict[str, Any] = None):
        self.name = name
        self.data = data or {}

    @abstractmethod
    def get_value(self) -> Any:
        pass

    @property
    def save_to_json(self) -> str:
        return f'"{self.name}":{{{{"json": {self.get_value().save_to_json()}}}}}}'

    def _load_from_file(self, file_name: str):
        import json
        try:
            with open(file_name, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    @property
    def items(self) -> Dict[str, Any]:
        return {key: value for key, value in self.data.items()}

class BaseFileSection(FileSection):
    def __init__(self, name: str, default_value=None):
        super().__init__(name)
        self.default_value = default_value

    @abstractmethod
    def get_value(self) -> Any:
        pass

class FileSectionUtil:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FileSection':
        if data is None:
            return None
        section_type = next((t for t in dir(FileSection) if isinstance(getattr(FileSection, t), type)), None)
        if section_type is not None and hasattr(getattr(FileSection, section_type), '_load_from_file'):
            file_section = FileSection(section_type.__name__)
            file_section._load_from_file(data)
            return file_section
        else:
            raise ValueError('Invalid file section')

from_json = json.loads