from cash.custom_types.router import TypeRouter
from cash.custom_types.validators import TypeValidator


def get_type_router_injector() -> TypeRouter:
    type_validator = TypeRouter(
        validators=[
            TypeValidator(int, r"^\d+$"),
            TypeValidator(float, r"^\d+.\d+$"),
            TypeValidator(str, ".*+")
        ]
    )
    return type_validator
