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


    def _get_size(self) -> int:
        try:
            return os.path.getsize(self.file_name)
        except FileNotFoundError:
            raise Exception(f"File {self.file_name} not found")

    def _set_size(self) -> None:
        self.size = _ensure_valid_file_size()
        _write_zero_bytes_to_file()

    def _content(self) -> str:
        return _load_content_from_file()


    def _set_content(self) -> None:
        self.content = _load_content_from_file()

    def _validate_file_name(self) -> None:
        if not os.path.isabs(self.file_name):
            raise ValueError("File name must be absolute path.")


def _ensure_valid_file_size() -> int:
    try:
        return int(input("Enter file size (int): "))
    except ValueError:
        raise Exception("Invalid file size")


def _write_zero_bytes_to_file() -> None:
    try:
        with open(self.file_name, 'wb') as file:
            file.write(b'\0' * self.size)
    except Exception as e:
        raise Exception(f"Failed to write zero bytes to file {self.file_name}: {str(e)}")


def _load_content_from_file() -> str:
    try:
        with open(self.file_name, 'rb') as file:
            return file.read().decode('utf-8')
    except FileNotFoundError:
        return ""
    except Exception as e:
        raise Exception(f"Failed to read content from file {self.file_name}: {str(e)}")