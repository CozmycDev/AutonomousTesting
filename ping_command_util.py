from abc import ABC, abstractmethod
import os

class File(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def write_bytes(self, data: bytes) -> None:
        pass

    @abstractmethod
    def read_bytes(self) -> bytes:
        pass

    @property
    def size(self) -> int:
        return self.get_size()

    @size.setter
    def size(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        self._size = value

    @property
    def content(self) -> str:
        return ""

    def __str__(self):
        return f"File(size={self.size}, content=None)"