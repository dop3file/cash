from dataclasses import dataclass

from storage.storage import Storage
from syntax.schemas import ExecutedCommand


@dataclass
class Executor:
    executed_command: ExecutedCommand
    storage: Storage

