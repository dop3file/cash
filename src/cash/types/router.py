import re

from types.validators import TypeValidator
from utils import Data


class TypeRouter:
    def __init__(self, validators: list[TypeValidator]):
        self.validators = validators

    def get_type(self, data: Data) -> type:
        for validator in self.validators:
            if re.fullmatch(validator.regexp, data):
                return validator.validate(data)
