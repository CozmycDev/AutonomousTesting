from abc import ABC, abstractmethod
import os

class File(ABC):
    def __init__(self, file_name: str):
        self.file_name = file_name
        self._validate_file_name()
        self.size = None
        self.content = None

    @property
    def size(self) -> int:
        return self._get_size()

    @size.setter
    def size(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        self.size = value
        self._set_size()

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Content must be a string.")
        self.content = value
        self._set_content()

    @property
    def is_empty(self) -> bool:
        return self.size == 0 or (self.content and len(self.content.strip()) == 0)

    @property
    def exists(self) -> bool:
        return os.path.exists(self.file_name)

    @property
    def absolute_path(self) -> str:
        return os.path.abspath(self.file_name)

    @property
    def is_empty_content(self) -> bool:
        return not self.content or len(self.content.strip()) == 0

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @staticmethod
    def _validate_file_name(file_name: str) -> None:
        if not os.path.isabs(file_name):
            raise ValueError("File name must be absolute path.")

    @staticmethod
    def _get_size(file_name: str) -> int:
        try:
            return os.path.getsize(file_name)
        except FileNotFoundError:
            raise Exception(f"File {file_name} not found")

    @staticmethod
    def _set_size(size: int, file_name: str) -> None:
        if size < 0:
            raise ValueError("File size must be non-negative.")
        File._validate_file_name(file_name)
        _ensure_valid_file_size = lambda file_name=file_name: int(input(f"Enter file size (int) for {file_name}: "))
        file_size = _ensure_valid_file_size()
        try:
            with open(file_name, 'wb') as file:
                file.write(b'\0' * file_size)
        except Exception as e:
            raise Exception(f"Failed to write zero bytes to file {file_name}: {str(e)}")

    @staticmethod
    def _load_content_from_file(file_name: str) -> str:
        try:
            with open(file_name, 'rb') as file:
                return file.read().decode('utf-8')
        except FileNotFoundError:
            return ""
        except Exception as e:
            raise Exception(f"Failed to read content from file {file_name}: {str(e)}")

    def __str__(self) -> str:
        return f"File(name={self.file_name}, size={self.size or 'None'}, content='{self.content or ''}')"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {'file_name': self.file_name, 'size': self.size, 'content': self.content}

    @classmethod
    def from_dict(cls, data: dict) -> 'File':
        file = cls(data['file_name'])
        file.size = data['size']
        file.content = data['content']
        return file