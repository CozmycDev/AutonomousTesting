from abc import ABC, abstractmethod
import json
from typing import Dict, Any

class FileSection(ABC):
    def __init__(self, name: str):
        self.name = name
        self.data = {}

    @abstractmethod
    def get_value(self) -> Any:
        pass

    @property
    def save_to_json(self) -> str:
        return f'"{self.name}":{{{{"json": {self.get_value().save_to_json()}}}}}}'

    def save_to_file(self, file_name: str):
        import json
        with open(file_name, "w") as file:
            json.dump({self.name: self.data}, file)

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

class StringFileSection(BaseFileSection):
    def __init__(self, name: str, default_value=""):
        super().__init__(name, default_value)

    def get_value(self) -> str:
        return self.data.get("value", self.default_value)

class IntFileSection(BaseFileSection):
    def __init__(self, name: str, default_value=0):
        super().__init__(name, default_value)

    def get_value(self) -> int:
        return self.data.get("value", self.default_value)

class BoolFileSection(BaseFileSection):
    def __init__(self, name: str, default_value=False):
        super().__init__(name, default_value)

    def get_value(self) -> bool:
        return self.data.get("value", self.default_value)

class PathFileSection(BaseFileSection):
    def __init__(self, name: str, default_value=""):
        super().__init__(name, default_value)

    def get_value(self) -> str:
        return self.data.get("path", self.default_value)

def load_file_config(config_name: str, file_section_types: Dict[str, type]) -> Dict:
    config = {}
    for section_type in file_section_types.values():
        section = FileSection.create(config, section_type.__name__)
        try:
            with open(f"{config_name}.{section.name}", "r") as file:
                config[section] = section_type().from_json(file.read())
        except FileNotFoundError:
            pass
    return config

def from_json(json_str: str) -> object:
    import json
    return json.loads(json_str)

#