import re
from typing import Optional

from cash.syntax.schemas import Token, TokenPipeline, TokenTypes


class Lexer:
    def __init__(self):
        self.tokens = TokenTypes()

    def analyze(self, command: str) -> TokenPipeline:
        token_pipeline = TokenPipeline(tokens=[])
        last_token = ""
        for char in command:
            last_token += char
            possible_token = self._parse_token(last_token)
            if possible_token is not None:
                token_pipeline.add(possible_token)
                last_token = ""
        return token_pipeline

    def _parse_token(self, possible_token: str) -> Optional[Token]:
        for token_type in self.tokens:
            if re.fullmatch(token_type.regexp, possible_token) is not None:
                return Token(token_type, possible_token)
        return None