import re

from cash.custom_types.validators import TypeValidator
from cash.utils import Key


class TypeRouter:
    def __init__(self, validators: list[TypeValidator]):
        # TODO: fixed it, in validators StringValidator must be in end of list
        self.validators = validators

    def get_type(self, data: Key) -> type:
        for validator in self.validators:
            if re.fullmatch(validator.regexp, data):
                return validator.validate(data)
        return str