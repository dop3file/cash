import time
from typing import Optional

from cash.exceptions import StorageNotFoundError
from cash.storage.schemas import Record
from cash.services import singleton, Key, Value


@singleton
class Storage:
    def __init__(self):
        self._storage: dict[Key, Record] = {}

    def get(self, key: Key) -> Record:
        try:
            return self._storage[key]
        except IndexError:
            raise StorageNotFoundError(f"Not found item by key: {key}")

    def set(self, key: Key, value: Value, ttl: Optional[int] = None) -> None:
        timestamp = int(time.time())
        self._storage[key] = Record(
            data=value,
            ttl=ttl,
            last_usage=timestamp,
            created_at=timestamp
        )

    def remove(self, key: Key) -> None:
        try:
            del self._storage[key]
        except IndexError:
            raise StorageNotFoundError(f"Not found item by key: {key}")
