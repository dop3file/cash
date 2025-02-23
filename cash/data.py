from dataclasses import dataclass
from typing import Protocol, Any


class DataType(Protocol):
    type: str
    regexp: str

    def __init__(self, data=None) -> None:
        self.data = data

    def to_python(self) -> Any:
        raise NotImplementedError


class Int(DataType):
    type = "int"
    regexp = r"\d+"

    def to_python(self) -> int:
        return int(self.data)


class Null(DataType):
    def to_python(self) -> None:
        return None


class List(DataType):
    def to_python(self) -> tuple[Any]:
        return self.data


parsing_data_types = (Int,)
