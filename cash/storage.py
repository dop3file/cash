from typing import Protocol

from cash.data import DataType, Null


class BaseStorage(Protocol):
    @classmethod
    def get(cls, key: str) -> DataType:
        raise NotImplementedError

    @classmethod
    def set(cls, key: str, value: DataType) -> None:
        raise NotImplementedError

    @classmethod
    def keys(cls) -> tuple[str]:
        raise NotImplementedError

    @classmethod
    def delete(cls, key: str) -> None:
        raise NotImplementedError


class Storage(BaseStorage):
    _storage: dict[str, DataType] = {}

    @classmethod
    def get(cls, key: str) -> DataType:
        return cls._storage[key]

    @classmethod
    def set(cls, key: str, value: DataType) -> None:
        cls._storage[key] = value

    @classmethod
    def keys(cls) -> tuple[str]:
        return tuple(cls._storage.keys())

    @classmethod
    def delete(cls, key: str) -> None:
        if key in cls._storage:
            del cls._storage[key]
