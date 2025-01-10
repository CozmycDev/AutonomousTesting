import os
from typing import Optional, Dict

class File:
    def __init__(self) -> None:
        self.config: Dict[str, str] = {
            'name': '',
            'content': '',
            'path': ''
        }
        self._config_lock = threading.Lock()

    def create(self, name: str, content: Optional[str] = None) -> None:
        if not name or not content:
            raise ValueError('Name and content are required')
        with self._config_lock:
            self.config['name'] = name
        try:
            file_path = os.path.join(os.getcwd(), name)
            if os.path.exists(file_path):
                raise FileExistsError(f'File {file_path} already exists')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            self._handle_error(e)

    def _update_file(self, path: str, new_name: str, content: Optional[str] = None) -> None:
        if not content and not new_name:
            raise ValueError('Content or name is required')
        try:
            file_path = os.path.join(os.getcwd(), new_name)
            with open(file_path, 'w') as file:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                file.write(content)
        except Exception as e:
            self._handle_error(e)

    def _delete_file(self) -> None:
        try:
            if not self.config['name']:
                raise ValueError('File does not exist')
            os.remove(os.path.join(os.getcwd(), self.config['name']))
        except Exception as e:
            self._handle_error(e)

    def delete(self) -> None:
        if not self.config['name']:
            raise ValueError('File does not exist')
        self._delete_file()

    @property
    def config(self) -> Dict[str, str]:
        return {key: value for key, value in self.config.items() if value}

    @config.setter
    def config(self, value: Dict[str, str]) -> None:
        if 'name' not in value:
            raise ValueError('Name is required')
        with self._config_lock:
            self.config = value