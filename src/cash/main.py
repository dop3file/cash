import asyncio

from database import Database
from server.server import Server
from syntax.lexer import Lexer


if __name__ == "__main__":
    server = Server("localhost", 8001, Database(Lexer()))
    asyncio.run(server.run_server())
    # lexer = Lexer()
    # print(lexer.analyze('GET "SLAVE"'))
