from cash.utils import Key
from cash.exceptions import ValidateError


class TypeValidator:
    def __init__(self, _type: type, regexp: str):
        self._type = _type
        self._regexp = regexp

    def validate(self, data: Key) -> type:
        try:
            self._type(data)
            return self._type
        except ValueError as e:
            raise ValidateError from e

    @property
    def regexp(self) -> str:
        return self._regexp
