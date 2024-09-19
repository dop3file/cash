import asyncio

from cash.database import Database
from cash.server.server import Server
from cash.syntax.lexer import Lexer
from cash.syntax.parser import Parser
from custom_types.injectors import get_type_router_injector
from custom_types.router import TypeRouter
from executor.executor import Executor
from storage.storage import Storage

if __name__ == "__main__":
    # server = Server("localhost", 8001, Database(Lexer()))
    # asyncio.run(server.run_server())
    lexer = Lexer()
    parser = Parser(
        lexer.analyze("GET \"slave\";")
    )
    executor = Executor(parser.parse(), Storage(), get_type_router_injector())
    executor.execute()
