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

    def __str__(self):
        return f"File(size={self.get_size()}, content=None)"

class PseudoFile(File):
    def __init__(self, size: int, content: str = "") -> None:
        self._size = size
        self._content = content

    @property
    def size(self) -> int:
        return self._size

    @property
    def content(self) -> str:
        return self._content

    def get_size(self) -> int:
        return self._size

    def write_bytes(self, data: bytes) -> None:
        raise NotImplementedError("This is a pseudo file and does not support writing")

    def read_bytes(self) -> bytes:
        raise NotImplementedError("This method should be overridden in child classes")