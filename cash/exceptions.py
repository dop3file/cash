from functools import wraps

from executor.utils import ExecutorResult


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


class StorageNotFoundError(CustomBaseError):
    pass


def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomBaseError as e:
            return ExecutorResult(error=e, value=None, log="")
        except Exception:
            return ExecutorResult(error=ServerError("Server unknown error"), value=None, log="")
    return wrapper