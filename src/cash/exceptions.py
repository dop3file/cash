class CustomBaseException(Exception):
    pass


class ParserException(CustomBaseException):
    pass


class NotRequiredToken(ParserException):
    pass


class ValidateError(CustomBaseException):
    pass