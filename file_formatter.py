import os
from typing import Optional

class File:
    NAME = 'file'
    PATH_FORMAT = '{os.getcwd()}/{name}'
    CONTENT = None
    EXIST_ERROR_MSG = f'File {path} already exists'

    def __init__(self) -> None:
        self._config: dict = {
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
        try:
            with open(path, 'w') as file:
                file.write(content)
        except Exception as e:
            self._handle_error(e)

    def _update_file(self, path: str, new_name: str, content: Optional[str] = None) -> None:
        if not content and not new_name:
            raise ValueError('Content or name is required')
        try:
            with open(path, 'w') as file:
                if new_name:
                    rel_path = os.path.join(os.path.dirname(path), new_name)
                else:
                    rel_path = path
                file.write(content)
        except Exception as e:
            self._handle_error(e)

    def _delete_file(self) -> None:
        try:
            os.remove(os.path.join(os.getcwd(), self.config['name']))
        except Exception as e:
            self._handle_error(e)

    def delete(self) -> None:
        if not self.config['name']:
            raise ValueError('File does not exist')
        self._delete_file()

    def _handle_error(self, error: Exception) -> None:
        print(error)
        # You can also add more logging or error handling here as needed

    @property
    def config(self) -> dict:
        return self._config

    @config.setter
    def config(self, value: dict) -> None:
        if 'name' not in value:
            raise ValueError('Name is required')
        self._config = value