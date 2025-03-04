from cash.core.operators import Get, Set
from cash.core.parser import Parser


def test_parse_get(parser: Parser):
    result = parser.parse("GET x")
    assert isinstance(result, Get)


def test_parse_set(parser: Parser):
    result = parser.parse("SET x 1")
    assert isinstance(result, Set)
