from typing import Callable

from exceptions import NotRequiredToken
from syntax.schemas import TokenPipeline, TokenType, TokenTypes, ExecutedCommand, Token


class Parser:
    def __init__(self, token_pipeline: TokenPipeline):
        self.pos = 0
        self.tokens = token_pipeline.tokens

    def parse(self) -> ExecutedCommand:
        operator_pos = self.operator_required()
        self.pos = operator_pos
        operator_args = self.find_operator_args()
        self.concrete_required(TokenTypes.SEMICOLON)
        executed_command = ExecutedCommand(
            operator=self.tokens[operator_pos],
            args=operator_args
        )
        return executed_command

    def find_operator_args(self) -> list[Token]:
        operator_args = []
        for tmp_position in range(self.pos, len(self.tokens) - 1):
            if self.tokens[tmp_position].is_arg:
                operator_args.append(self.tokens[tmp_position])
        return operator_args

    def _required(self, rule: Callable) -> int:
        pos = self.pos
        while not rule(self.tokens[self.pos]):
            pos += 1

        if rule(self.tokens[self.pos]):
            raise NotRequiredToken("Required token not found.")
        return pos

    def concrete_required(self, token_type: TokenType) -> int:
        return self._required(lambda token: token.type == token_type)

    def operator_required(self) -> int:
        return self._required(lambda token: token.is_operator)
