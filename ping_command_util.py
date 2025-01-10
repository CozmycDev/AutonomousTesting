from abc import ABC, abstractmethod
import os
import socket
import struct

class File(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def write_bytes(self, data: bytes) -> None:
        pass

class PseudoFile(File):
    def __init__(self, size: int, content: str = "") -> None:
        self._size = size
        self._content = content

    def get_size(self) -> int:
        return self._size

    def write_bytes(self, data: bytes) -> None:
        raise NotImplementedError("This is a pseudo file and does not support writing")

class FileIO:
    @staticmethod
    def read_file(path: str):
        with open(path, "rb") as f:
            content = f.read()
            return content

    @staticmethod
    def write_bytes(path: str, data: bytes) -> None:
        with open(path, "wb") as f:
            f.write(data)

class PingCommandUtil:
    # Other functionality and methods remain the same.

    @staticmethod
    def get_pseudo_file():
        return PseudoFile(1024)
        
    @staticmethod
    def write_to_file(data: bytes):
        file_path = '/dev/null'
        FileIO.write_bytes(file_path, data)