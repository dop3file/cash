from dataclasses import dataclass
from typing import Optional

from cash.exceptions import CustomBaseError
from cash.syntax.schemas import Token
from cash.utils import Value, OK_STATUS


@dataclass
class Command:
    operator: Token
    args: list[Token]


@dataclass
class ExecutorResult:
    error: Optional[CustomBaseError] = None
    value: Optional[Value] = None
    log: str = OK_STATUS
