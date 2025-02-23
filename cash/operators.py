from enum import Enum
from typing import Protocol, Any

from cash.arguments import Argument, ArgumentType
from cash.data import DataType, Null, List
from cash.exceptions import InvalidArgument
from cash.storage import BaseStorage


class Operator(Protocol):
    regexp: str

    def __init__(self, arguments: tuple[Argument]):
        self._arguments = arguments

    def execute(self, storage: BaseStorage, *args, **kwargs) -> Any:
        raise NotImplementedError


class Get(Operator):
    regexp = "GET"

    def execute(self, storage: BaseStorage, *args, **kwargs) -> DataType:
        return storage.get(key=self._arguments[0].data)


class Set(Operator):
    regexp = "SET"

    def execute(self, storage: BaseStorage, *args, **kwargs) -> Null:
        storage.set(key=self._arguments[0].data, value=self._arguments[1].data)
        return Null()


class Keys(Operator):
    regexp = "KEYS"

    def execute(self, storage: BaseStorage, *args, **kwargs) -> Any:
        return List(storage.keys())


class Delete(Operator):
    regexp = "DEL"

    def execute(self, storage: BaseStorage, *args, **kwargs) -> Any:
        if len(self._arguments) == 0:
            raise InvalidArgument("Not enough arguments(one or more).")
        for argument in self._arguments:
            storage.delete(argument.data)
        return Null()


class FlushAll(Operator):
    regexp = "FLUSHALL"

    def __init__(self, arguments: tuple[Argument]):
        super().__init__(arguments)
        self._keys_operator = Keys(tuple())

    def execute(self, storage: BaseStorage, *args, **kwargs) -> Any:
        keys = self._keys_operator.execute(storage).to_python()
        if len(keys) == 0:
            return Null()
        arguments = tuple(
            [Argument(type=ArgumentType.SYSTEM, data=key) for key in keys]
        )
        Delete(arguments).execute(storage)

        return Null()


class OperatorEnum(Enum):
    GET = Get
    SET = Set
    KEYS = Keys
    FLUSH_ALL = FlushAll
    DELETE = Delete
