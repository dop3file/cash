from dataclasses import dataclass

from loguru import logger

from cash.executor.utils import ExecutorResult, Command
from cash.storage.storage import Storage
from cash.custom_types.router import TypeRouter


@dataclass
class Executor:
    executed_command: Command
    storage: Storage
    type_router: TypeRouter

    def execute(self) -> ExecutorResult:
        logger.debug(self.executed_command)



