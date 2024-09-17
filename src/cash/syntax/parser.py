from typing import Callable

from exceptions import NotRequiredToken
from syntax.schemas import TokenPipeline, TokenType, TokenTypes


class Parser:
    def __init__(self, token_pipeline: TokenPipeline):
        self.pos = 0
        self.tokens = token_pipeline.tokens

    def parse(self, token_pipeline: TokenPipeline):
        operator_pos = self.operator_required()
        self.pos = operator_pos

        self.concrete_required(TokenTypes.SEMICOLON)

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
        return self._required(lambda token: token.is_operator())
