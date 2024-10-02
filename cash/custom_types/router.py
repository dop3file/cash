import re

from cash.custom_types.validators import TypeValidator
from cash.services import Key, Value


class TypeRouter:
    def __init__(self, validators: list[TypeValidator]):
        # TODO: fixed it, in validators StringValidator must be in end of list
        self.validators = validators

    def get_type(self, data: Key) -> type:
        for validator in self.validators:
            if re.fullmatch(validator.regexp, data):
                return validator.validate(data)
        return str

    def prepare_data(self, data: Key) -> Key:
        if len(data) < 2:
            raise TypeError("Data without quoutes")
        return data[1:-1]

    def get_value(self, data: Key) -> Value:
        data = self.prepare_data(data)
        value: Value = self.get_type(data)(data)
        return value
