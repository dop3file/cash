from abc import ABC, abstractmethod

from cash.executor.services import ExecutorResult
from cash.storage.storage import Storage
from cash.syntax.schemas import Token
from cash.exceptions import NotEnoughError, InvalidArgument
from cash.custom_types.router import TypeRouter


class ExecutorOperator(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self) -> ExecutorResult:
        raise NotImplementedError


class Get(ExecutorOperator):
    def __init__(self, *args, **kwargs):
        self._args: list[Token] = kwargs["args"]
        self._storage: Storage = kwargs["storage"]
        self._type_router: TypeRouter = kwargs["type_router"]

    def execute(self) -> ExecutorResult:
        try:
            # TODO: mypy fixes and finish DATA logic, because .data its token
            key = self._args[0].data
            if key is None:
                raise InvalidArgument("Invalid argument.")
            real_key = str(self._type_router.get_value(key))
            record = self._storage.get(real_key)
            return ExecutorResult(
                value=record.data
            )
        except IndexError:
            raise NotEnoughError("Not enough arguments for GET operator")
        except AttributeError:
            raise InvalidArgument(f"Invalid argument: expected DATA but received {self._args[0].type}")


class Ping(ExecutorOperator):
    MESSAGE = "PONG"

    def __init__(self, *args, **kwargs) -> None:
        pass

    def execute(self) -> ExecutorResult:
        return ExecutorResult(
            value="PONG"
        )
