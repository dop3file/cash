from typing import TypeAlias, Any, Callable


Key: TypeAlias = str
Value: TypeAlias = float | int | str
OK_STATUS = "OK"


def singleton(class_: type) -> Callable:
    instances = {}

    def getinstance(*args: tuple[Any], **kwargs: dict[str, Any]) -> object:
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance