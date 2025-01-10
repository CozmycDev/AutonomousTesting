import os
from typing import Optional

class File:
    NAME = 'file'
    PATH_FORMAT = '{os.getcwd()}/{name}'
    CONTENT = None
    EXIST_ERROR_MSG = f'File {path} already exists'

    def __init__(self):
        self._config = {
            'name': '',
            'content': '',
            'path': ''
        }

    def create(self, name: str, content: Optional[str] = None) -> None:
        if not name:
            raise ValueError('Name is required')
        self.path = os.path.join(os.getcwd(), name)
        if os.path.exists(self.path):
            raise FileExistsError(self.EXIST_ERROR_MSG.format(path=self.path))
        self._config['name'] = name
        self._config['content'] = content or ''
        with open(self.path, 'w') as file:
            file.write(self._config['content'])

    def update(self, name: Optional[str] = None, content: Optional[str] = None) -> None:
        if not self.name:
            raise ValueError('Name is required')
        new_name = name or self.config.get('name')
        path = os.path.join(self.path, new_name) if new_name else self.path
        if os.path.exists(path):
            raise FileExistsError(self.EXIST_ERROR_MSG.format(path=path))
        self._config['name'] = new_name
        self._config['content'] = content or ''
        with open(self.path, 'w') as file:
            file.write(self._config['content'])

    def delete(self) -> None:
        if not self.path:
            raise ValueError('File does not exist')
        os.remove(self.path)

    @property
    def config(self) -> dict:
        return self._config

    @config.setter
    def config(self, value: dict) -> None:
        self._config = value