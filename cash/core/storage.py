from typing import Protocol, Any

from cash.core.data_types import DataType
from cash.core.exceptions import KeyNotFound
from cash.core.data_types import CashValue


class IStorage(Protocol):
    @classmethod
    def get(cls, key: str) -> DataType:
        raise NotImplementedError

    @classmethod
    def set(cls, key: str, value: DataType, ttl: int | None = None) -> None:
        raise NotImplementedError

    @classmethod
    def keys(cls) -> tuple[str]:
        raise NotImplementedError

    @classmethod
    def delete(cls, key: str) -> None:
        raise NotImplementedError

    @classmethod
    def values(cls) -> tuple[CashValue]:
        raise NotImplementedError

    @classmethod
    def evaluate(cls, expression: str) -> Any:
        raise NotImplementedError


class Storage(IStorage):
    _storage: dict[str, CashValue] = {}

    @classmethod
    def get(cls, key: str) -> DataType:
        try:
            return cls._storage[key].data_type
        except KeyError:
            raise KeyNotFound(f"Item with {key} not found.")

    @classmethod
    def set(cls, key: str, value: DataType, ttl: int | None = None) -> None:
        cls._storage[key] = CashValue(
            data_type=value,
            key=key,
            ttl=ttl
        )

    @classmethod
    def keys(cls) -> tuple[str]:
        return tuple(cls._storage.keys())

    @classmethod
    def values(cls) -> tuple[CashValue]:
        return tuple(cls._storage.values())

    @classmethod
    def delete(cls, key: str) -> None:
        if key in cls._storage:
            del cls._storage[key]

    @classmethod
    def evaluate(cls, expression: str) -> Any:
        return eval(
            expression,
            {key: value.data_type.to_python() for (key, value) in cls._storage.items()}
        )
