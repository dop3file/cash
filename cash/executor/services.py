from dataclasses import dataclass, asdict
from typing import Optional

from cash.exceptions import CustomBaseError
from cash.syntax.schemas import Token
from cash.services import Value, OK_STATUS


@dataclass
class Command:
    operator: Token
    args: list[Token]


@dataclass
class ExecutorResult:
    error: Optional[CustomBaseError] = None
    value: Optional[Value] = None
    log: str = OK_STATUS

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}