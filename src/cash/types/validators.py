from typing import Protocol, Optional

from utils import Data
from exceptions import ValidateError


class TypeValidator(Protocol):
    def __init__(self, _type: type):
        self._type = _type

    def validate(self, data: Data) -> type:
        raise NotImplemented

    @property
    def regexp(self) -> str:
        raise NotImplemented


class IntValidator(TypeValidator):
    def __init__(self):
        _type = int
        super().__init__(_type)

    def validate(self, data: Data) -> type:
        try:
            int(data)
            return self._type
        except ValueError as e:
            raise ValidateError from e

    @property
    def regexp(self) -> str:
        return r"^\d+$"


class FloatValidator(TypeValidator):
    def __init__(self):
        _type = float
        super().__init__(_type)

    def validate(self, data: Data) -> type:
        try:
            float(data)
            return self._type
        except ValueError as e:
            raise ValidateError from e

    @property
    def regexp(self) -> str:
        return r"^\d+.\d+$"


class StringValidator(TypeValidator):
    def __init__(self):
        _type = str
        super().__init__(_type)

    def validate(self, data: Data) -> type:
        return self._type

    @property
    def regexp(self) -> str:
        return ".*+"
