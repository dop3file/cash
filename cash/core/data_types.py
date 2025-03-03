import time
from dataclasses import dataclass, field
from typing import Protocol, Any, runtime_checkable


@runtime_checkable
class DataType(Protocol):
    type: str
    regexp: str

    def __init__(self, data: Any = None, message: str | None = None) -> None:
        self.data = data
        self.message = message

    def to_python(self) -> Any:
        raise NotImplementedError

    def get_message(self) -> str | None:
        return self.message


class Int(DataType):
    type = "int"
    regexp = r"\d+"

    def to_python(self) -> int:
        return int(self.data)


class String(DataType):
    type = "string"
    regexp = r'^"[^"\\]*(?:\\.[^"\\]*)*"'

    def to_python(self) -> str:
        without_quotes = slice(1, -1)
        return self.data[without_quotes]


class Null(DataType):
    def to_python(self) -> None:
        return None


class List(DataType):
    def to_python(self) -> tuple[Any]:
        return self.data


class Evaluated(DataType):

    def to_python(self) -> Any:
        if isinstance(self.data, CashValue):
            return self.data.data_type.to_python()
        return self.data

@dataclass
class CashResult:
    error: str | None = None
    result: str | None = None
    message: str | None = None


@dataclass
class CashValue:
    data_type: DataType
    key: str
    ttl: int | None = field(default=None)
    creation_timestamp: float = field(default_factory=time.time)

    def is_expired(self) -> bool:
        if self.ttl is None:
            return False
        return time.time() - self.creation_timestamp > self.ttl


parsing_data_types = (Int, String)
