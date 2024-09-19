from abc import ABC, abstractmethod

from cash.executor.utils import ExecutorResult
from cash.storage.storage import Storage
from cash.syntax.schemas import Token
from cash.exceptions import NotEnoughError, InvalidArgument


class ExecutorOperator(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self):
        raise NotImplementedError


class GET(ExecutorOperator):
    def __init__(self, *args, **kwargs):
        self._args: list[Token] = kwargs["args"]
        self._storage: Storage = kwargs["storage"]

    def execute(self) -> ExecutorResult:
        try:
            # TODO: mypy fixes and finish DATA logic, because .data its token
            record = self._storage.get(self._args[0].data)
            return ExecutorResult(
                value=record.data
            )
        except IndexError:
            raise NotEnoughError("Not enough arguments for GET operator")
        except AttributeError:
            raise InvalidArgument(f"Invalid argument: expected DATA but received {self._args[0].type}")
