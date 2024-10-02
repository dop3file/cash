class CustomBaseError(Exception):
    pass


class ServerError(CustomBaseError):
    ...


class ParserException(CustomBaseError):
    pass


class NotRequiredToken(ParserException):
    pass


class ValidateError(CustomBaseError):
    pass


class StorageError(CustomBaseError):
    pass


class StorageNotFoundError(StorageError):
    pass


class ExecutorError(CustomBaseError):
    pass


class NotEnoughError(CustomBaseError):
    pass


class InvalidArgument(CustomBaseError):
    pass


class InvalidOperator(CustomBaseError):
    pass


class TypeError(CustomBaseError):
    pass
