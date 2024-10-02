from dataclasses import dataclass


from cash.executor.services import ExecutorResult, Command
from cash.storage.storage import Storage
from cash.custom_types.router import TypeRouter
from cash.exceptions import InvalidOperator
from cash.executor.operators import Get, Ping, ExecutorOperator


@dataclass
class Executor:
    executed_command: Command
    storage: Storage
    type_router: TypeRouter
    operators = {
        "GET": Get,
        "PING": Ping
    }

    def execute(self) -> ExecutorResult:
        def raise_invalid_operator(*args, **kwargs):
            raise InvalidOperator(f"Operator without realization: {self.executed_command.operator.type.name}")

        operator_class = self.operators.get(
            self.executed_command.operator.type.name,
            raise_invalid_operator,
        )
        operator: ExecutorOperator = operator_class(
            args=self.executed_command.args,
            storage=self.storage,
            type_router=self.type_router
        )

        return operator.execute()



