from cash.core.storage import IStorage


class AOFManager:
    def __init__(self, storage: IStorage) -> None:
        self._storage = storage

    def append(self):
        ...


class RDBManager:
    ...