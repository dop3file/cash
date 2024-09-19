from abc import ABC, abstractmethod

from executor.utils import ExecutorResult
from storage.storage import Storage
from syntax.schemas import Token
from utils import Key


class ExecutorOperator(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self):
        raise NotImplemented


class GET(ExecutorOperator):
    def __init__(self, *args, **kwargs):
        self._args: list[Token] = kwargs["args"]
        self._storage: Storage = kwargs["storage"]

    def execute(self) -> ExecutorResult:
        try:
            record = self._storage.get(self._args[0].data)
            return ExecutorResult(
                value=record.data
            )
        except IndexError as e:
            ...
