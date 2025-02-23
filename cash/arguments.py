from dataclasses import dataclass
from enum import StrEnum, auto

from cash.data import DataType


class ArgumentType(StrEnum):
    SYSTEM = auto()
    LITERAL = auto()


@dataclass
class Argument:
    type: ArgumentType
    data: DataType | str
