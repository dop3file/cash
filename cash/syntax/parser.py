from typing import Callable

from cash.exceptions import NotRequiredToken
from cash.syntax.schemas import TokenPipeline, TokenType, TokenTypes, Token
from cash.executor.services import Command


class Parser:
    def __init__(self):
        self.pos = 0
        self.tokens = TokenPipeline([])

    def parse(self, token_pipeline: TokenPipeline) -> Command:
        self.tokens = token_pipeline.tokens
        operator_pos = self.operator_required()
        self.pos = operator_pos
        operator_args = self.find_operator_args()
        self.concrete_required(TokenTypes.SEMICOLON)
        executed_command = Command(
            operator=self.tokens[operator_pos],
            args=operator_args
        )
        return executed_command

    def find_operator_args(self) -> list[Token]:
        operator_args = []
        for tmp_position in range(self.pos, len(self.tokens)):
            if self.tokens[tmp_position].is_arg:
                operator_args.append(self.tokens[tmp_position])
        return operator_args

    def _required(self, rule: Callable) -> int:
        pos: int = self.pos
        while not rule(self.tokens[self.pos]) and pos < len(self.tokens) - 1:
            pos += 1

        if not rule(self.tokens[pos]):
            raise NotRequiredToken
        return pos

    def concrete_required(self, token_type: TokenType) -> int:
        try:
            return self._required(lambda token: token.type == token_type)
        except NotRequiredToken:
            raise NotRequiredToken(f"Required token not found: expected {token_type.name}")

    def operator_required(self) -> int:
        return self._required(lambda token: token.is_operator)
