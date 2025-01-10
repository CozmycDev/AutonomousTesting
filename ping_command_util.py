from abc import ABC, abstractmethod
import os

class File(ABC):
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._size = None
        self._content = None

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