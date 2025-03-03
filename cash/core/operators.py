from enum import Enum
from typing import Protocol, Any, runtime_checkable

from cash.core.arguments import Argument, ArgumentType
from cash.core.data_types import DataType, Null, List, Evaluated
from cash.core.exceptions import InvalidArgument, NotEnoughArguments
from cash.core.storage import IStorage


@runtime_checkable
class Operator(Protocol):
    regexp: str

    def __init__(self, arguments: tuple[Argument]):
        self._arguments = arguments

    def execute(self, storage: IStorage, *args, **kwargs) -> Any:
        raise NotImplementedError


class Get(Operator):
    regexp = "GET"

    def execute(self, storage: IStorage, *args, **kwargs) -> DataType:
        return storage.get(key=self._arguments[0].data)


class Set(Operator):
    regexp = "SET"

    def execute(self, storage: IStorage, *args, **kwargs) -> Null:
        if len(self._arguments) < 2:
            raise NotEnoughArguments("Not enough arguments.")
        key = self._arguments[0]
        value = self._arguments[1]
        ttl = self._arguments[2].data.to_python() if len(self._arguments) == 3 else None
        if value.type == ArgumentType.SYSTEM:
            raise InvalidArgument(f"Invalid argument for set: {value.data}")
        storage.set(key=key.data, value=value.data, ttl=ttl)
        return Null()


class Keys(Operator):
    regexp = "KEYS"

    def execute(self, storage: IStorage, *args, **kwargs) -> Any:
        return List(storage.keys())


class Delete(Operator):
    regexp = "DEL"

    def execute(self, storage: IStorage, *args, **kwargs) -> Any:
        if len(self._arguments) == 0:
            raise NotEnoughArguments("Not enough arguments(one or more).")
        for argument in self._arguments:
            storage.delete(argument.data)
        return Null()


class FlushAll(Operator):
    regexp = "FLUSHALL"

    def __init__(self, arguments: tuple[Argument]):
        super().__init__(arguments)
        self._keys_operator = Keys(tuple())

    def execute(self, storage: IStorage, *args, **kwargs) -> Any:
        keys = self._keys_operator.execute(storage).to_python()
        if len(keys) == 0:
            return Null()
        arguments = tuple(
            [Argument(type=ArgumentType.SYSTEM, data=key) for key in keys]
        )
        Delete(arguments).execute(storage)

        return Null(message=f"Deleted {len(arguments)} keys.")


class Ping(Operator):
    regexp = "PING"

    def execute(self, storage: IStorage, *args, **kwargs) -> Any:
        return Null(message="PONG")


class Eval(Operator):
    regexp = "EVAL"

    def execute(self, storage: IStorage, *args, **kwargs) -> Any:
        return Evaluated(
            data=storage.evaluate(
                "".join(
                    [str(argument.data.to_python()) if isinstance(
                        argument.data, DataType
                    ) else str(argument.data) for argument in self._arguments[:]]
                )
            )
        )


class OperatorEnum(Enum):
    GET = Get
    SET = Set
    KEYS = Keys
    FLUSH_ALL = FlushAll
    DELETE = Delete
    PING = Ping
    EVAL = Eval

