from functools import wraps
from typing import Callable, Any

from cash.exceptions import CustomBaseError, ServerError
from cash.executor.services import ExecutorResult


def error_handler(func) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except CustomBaseError as e:
            return ExecutorResult(error=e, value=None, log="")
        except Exception:
            return ExecutorResult(error=ServerError("Server unknown error"), value=None, log="")
    return wrapper