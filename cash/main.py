import asyncio

from cash.syntax.lexer import Lexer
from cash.syntax.parser import Parser
from cash.storage.storage import Storage
from cash.database import Database
from cash.server.server import Server

if __name__ == "__main__":
    ...
    database = Database(
        Lexer(),
        Parser(),
        Storage()
    )
    server = Server("localhost", 8001, database)
    asyncio.run(server.run_server())
    # lexer = Lexer()
    # parser = Parser(
    #     lexer.analyze("PING;")
    # )
    # executor = Executor(parser.parse(), Storage(), get_type_router_injector())
    # print(executor.execute())
