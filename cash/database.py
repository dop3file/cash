import asyncio
from typing import Callable

#from cash.exceptions import EmptyTokensList
from cash.syntax.lexer import Lexer
from cash.custom_types.injectors import get_type_router_injector
from cash.executor.executor import Executor
from cash.executor.services import ExecutorResult
from cash.storage.storage import Storage
from cash.syntax.parser import Parser
from loguru import logger


class Database:
    def __init__(self, lexer: Lexer, parser: Parser, storage: Storage):
        self.lexer = lexer
        self.parser = parser
        self.storage = storage

    async def execute_command(self, input_command: str) -> ExecutorResult:
        tokens = self.lexer.analyze(input_command)
        if len(tokens.tokens) == 0:
            # Не разобрался как работает хэндлер exception`ов
            # TODO: raise EmptyTokensList(exception_message)
            exception_message = "The list of tokens cannot be empty!"
            logger.error(f"EmptyTokensList({exception_message})")
            return ExecutorResult(exception_message, value=None, log="")
        
        command = self.parser.parse(
            tokens
        )
        executor = Executor(
            command,
            self.storage,
            get_type_router_injector()
        )
        return executor.execute()

    async def execute_planning_tasks(self):
        pass # too much flood
        # await self.planning_task(lambda: print(1), 1)

    async def planning_task(self, func: Callable, every_n_seconds: int, *args, **kwargs):
        async def wrapper() -> None:
            while True:
                func(*args, **kwargs)
                await asyncio.sleep(every_n_seconds)

        task = asyncio.create_task(wrapper())
        await task
