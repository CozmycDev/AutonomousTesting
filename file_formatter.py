import os
from typing import Optional

class File:
    NAME = 'file'
    PATH_FORMAT = '{os.getcwd()}/{name}'
    CONTENT = None
    EXIST_ERROR_MSG = f'File {path} already exists'

    def __init__(self):
        self.config: dict = {
            'name': '',
            'content': '',
            'path': ''
        }

    def create(self, name: str, content: Optional[str] = None) -> None:
        if not name or not content:
            raise ValueError('Name and content are required')
        self._create_file(name, content)
        self.config['name'] = name

    def _create_file(self, name: str, content: str) -> None:
        path = os.path.join(os.getcwd(), name)
        if os.path.exists(path):
            raise FileExistsError(self.EXIST_ERROR_MSG.format(path=path))
        with open(path, 'w') as file:
            file.write(content)

    def update(self, name: Optional[str] = None, content: Optional[str] = None) -> None:
        if not self.config['name']:
            raise ValueError('Name is required')
        new_name = name or self.config.get('name')
        path = os.path.join(os.getcwd(), new_name) if new_name else os.getcwd()
        if os.path.exists(path):
            raise FileExistsError(self.EXIST_ERROR_MSG.format(path=path))
        self._update_file(path, new_name, content)
        self.config['name'] = new_name

    def _update_file(self, path: str, new_name: str, content: Optional[str] = None) -> None:
        if not content and not new_name:
            raise ValueError('Content or name is required')
        with open(path, 'w') as file:
            if new_name:
                rel_path = os.path.join(os.path.dirname(path), new_name)
            else:
                rel_path = path
            file.write(content)

    def delete(self) -> None:
        if not self.config['name']:
            raise ValueError('File does not exist')
        os.remove(os.path.join(os.getcwd(), self.config['name']))

    @property
    def config(self) -> dict:
        return self._config

    @config.setter
    def config(self, value: dict) -> None:
        self._config = value