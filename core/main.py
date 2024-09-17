
from core.syntax.lexer import Lexer


if __name__ == "__main__":
    # server = Server("localhost", 8001)
    # asyncio.run(server.run_server())
    lexer = Lexer()
    print(lexer.analyze('GET "SLAVE"'))
