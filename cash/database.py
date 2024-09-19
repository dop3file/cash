import asyncio
from typing import Callable

from cash.syntax.lexer import Lexer


class Database:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

    async def execute_command(self):
        ...

    async def execute_planning_tasks(self):
        await self.planning_task(lambda: print(1), 1)

    async def planning_task(self, func: Callable, every_n_seconds: int, *args, **kwargs):
        async def wrapper() -> None:
            while True:
                func(*args, **kwargs)
                await asyncio.sleep(every_n_seconds)

        task = asyncio.create_task(wrapper())
        await task
