import re
from typing import Type

from cash.arguments import Argument, ArgumentType
from cash.data import parsing_data_types
from cash.exceptions import InvalidOperator
from cash.operators import Operator, OperatorEnum


class Parser:
    def __init__(self):
        self.query_pointer = 0

    def _parse_operator(self, query_operator: str) -> Type[Operator]:
        for operator in OperatorEnum:
            if operator.value.regexp == query_operator:
                return operator.value
        raise InvalidOperator(f"Invalid operator: {query_operator}")

    def _scan_until_space(self, query: str) -> str:
        result = ""
        char = self.query_pointer
        while char < len(query) and query[char] != " ":
            result += query[char]
            char += 1
        self.query_pointer = char + 1
        return result

    def _parse_argument(self, query_argument: str) -> Argument:
        for data_type in parsing_data_types:
            if re.fullmatch(data_type.regexp, query_argument):
                return Argument(
                    type=ArgumentType.LITERAL, data=data_type(query_argument)
                )
        return Argument(type=ArgumentType.SYSTEM, data=query_argument)

    def _parse_arguments(self, query: str) -> tuple[Argument, ...]:
        arguments = []
        while self.query_pointer < len(query):
            raw_argument = self._scan_until_space(query)
            arguments.append(self._parse_argument(raw_argument))
        return tuple(arguments)

    def parse(self, query: str) -> Operator:
        self.query_pointer = 0
        operator = self._parse_operator(self._scan_until_space(query))
        arguments = self._parse_arguments(query)
        return operator(
            arguments,
        )
