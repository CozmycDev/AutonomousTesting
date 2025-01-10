from typing import Optional, Dict
import threading
import os
from pathlib import Path
import logging
import json

class File:
    def __init__(self) -> None:
        self._config: Dict[str, str] = {
            'name': '',
            'content': '',
            'path': ''
        }
        self._lock = threading.Lock()
        self._logger = logging.getLogger(__name__)

    def create(self, name: str, content: Optional[str] = None) -> None:
        if not name or not content:
            raise ValueError('Name and content are required')
        with self._lock:
            self._config['name'] = name
            self._config['content'] = content

        file_path = Path(os.getcwd()) / name
        file_path.parent.mkdir(exist_ok=True)
        try:
            file_path.write_text(self._config['content'])
        except Exception as e:
            self._handle_error(e)

    def update_file(self, new_name: str, content: Optional[str] = None) -> None:
        if not content and not new_name:
            raise ValueError('Content or name is required')
        file_path = Path(os.getcwd()) / new_name
        file_path.parent.mkdir(exist_ok=True)
        try:
            file_path.write_text(content if content else self._config['content'])
        except Exception as e:
            self._handle_error(e)

    def delete_file(self) -> None:
        try:
            os.remove(Path(os.getcwd()) / self._config['name'])
        except Exception as e:
            self._handle_error(e)

    def delete(self) -> None:
        if not self._config['name']:
            raise ValueError('File does not exist')
        self.delete_file()

    @property
    def config(self) -> Dict[str, str]:
        return {key: value for key, value in self._config.items() if value}

    @config.setter
    def config(self, value: Dict[str, str]) -> None:
        if 'name' not in value:
            raise ValueError('Name is required')
        with self._lock:
            self._config = value

    def load_config(self, name: str) -> bool:
        """Loads file configuration from the given name."""
        self._config['name'] = name
        try:
            file_path = Path(os.getcwd()) / name
            if not file_path.exists():
                raise FileNotFoundError(f'File {name} does not exist')
            with open(file_path, 'r') as f:
                json_data = json.load(f)
            self.config = {'name': name, **json_data}
            return True
        except Exception as e:
            print(f"Error loading configuration: {e}")
            return False

    def save_config(self) -> None:
        """Saves the current configuration to the file."""
        try:
            file_path = Path(os.getcwd()) / self._config['name']
            if os.path.exists(file_path):
                os.remove(file_path)
            with open(file_path, 'w') as f:
                json.dump(self.config, f)
        except Exception as e:
            print(f"Error saving configuration: {e}")