from dataclasses import dataclass
from typing import Optional


@dataclass
class TokenType:
    name: str
    regexp: str
    strong: bool
    is_operator: bool
    is_arg: bool = False


@dataclass
class Token:
    type: TokenType
    data: Optional[str] = None

    @property
    def is_operator(self) -> bool:
        return self.type.is_operator

    @property
    def is_arg(self) -> bool:
        return self.type.is_arg


@dataclass
class TokenPipeline:
    tokens: list[Token]

    def add(self, token: Token) -> None:
        self.tokens.append(token)


class TokenTypes:
    GET = TokenType("GET", "GET", strong=True, is_operator=True)
    SET = TokenType("SET", "SET", strong=True, is_operator=True)
    WHITESPACE = TokenType("WHITESPACE", r"\s", strong=False, is_operator=False)
    DATA = TokenType("DATA", r"\".*?\"", strong=False, is_operator=False, is_arg=True)
    SEMICOLON = TokenType("SEMICOLON", ";", strong=True, is_operator=False)

    def __iter__(self):
        for var in vars(TokenTypes):
            if not var.startswith("__"):
                yield self.__getattribute__(var)


