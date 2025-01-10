from abc import ABC, abstractmethod
import os

class File(ABC):
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._size = None
        self._content = None
        self._validate_file_name()

    @property
    def size(self) -> int:
        return self._get_size()

    @size.setter
    def size(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        self._set_size(value)

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Content must be a string.")
        self._content = value

    @property
    def is_empty(self) -> bool:
        return self.size == 0 or (self.content and len(self.content.strip()) == 0)

    @property
    def exists(self) -> bool:
        return os.path.exists(self.file_name)

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        self._validate_file_name()
        self._file_name = value

    @property
    def is_empty_content(self) -> bool:
        return not self.content or len(self.content.strip()) == 0

    @property
    def absolute_path(self) -> str:
        return os.path.abspath(self.file_name)

    def __str__(self):
        return f"File(size={self.size}, content=None)"

    def _get_size(self) -> int:
        try:
            with open(self._file_name, 'rb') as file:
                return os.path.getsize(file.name)
        except FileNotFoundError:
            raise Exception(f"File {self._file_name} not found")

    def _set_size(self, size: int) -> None:
        self._size = size
        try:
            with open(self._file_name, 'wb') as file:
                file.write(b'\0' * size)
        except Exception as e:
            raise Exception(f"Failed to set file size {self._file_name}: {str(e)}")

    def read_bytes(self) -> bytes:
        try:
            with open(self._file_name, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"File {self._file_name} not found")
        except Exception as e:
            raise Exception(f"Failed to read file {self._file_name}: {str(e)}")

    def write_bytes(self, data: bytes) -> None:
        try:
            with open(self._file_name, 'wb') as file:
                file.write(data)
        except Exception as e:
            raise Exception(f"Failed to write to file {self._file_name}: {str(e)}")

    def save(self) -> None:
        if not os.path.exists(os.path.dirname(self.file_name)):
            os.makedirs(os.path.dirname(self.file_name))
        try:
            with open(self._file_name, 'wb') as file:
                file.write(b'\0' * self.size)
        except Exception as e:
            raise Exception(f"Failed to save file {self._file_name}: {str(e)}")

    def load(self) -> None:
        if not os.path.exists(os.path.dirname(self.file_name)):
            os.makedirs(os.path.dirname(self.file_name))
        try:
            with open(self._file_name, 'rb') as file:
                self.size = os.path.getsize(file.name)
                self.content = file.read().decode('utf-8')
        except FileNotFoundError:
            raise Exception(f"File {self._file_name} not found")
        except Exception as e:
            raise Exception(f"Failed to load file {self._file_name}: {str(e)}")

    def delete(self) -> None:
        try:
            os.remove(self.file_name)
        except OSError as e:
            raise Exception(f"Failed to delete file {self._file_name}: {str(e)}")