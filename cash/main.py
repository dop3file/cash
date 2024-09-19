
from cash.syntax.lexer import Lexer
from cash.syntax.parser import Parser
from cash.custom_types.injectors import get_type_router_injector
from cash.executor.executor import Executor
from cash.storage.storage import Storage

if __name__ == "__main__":
    # server = Server("localhost", 8001, Database(Lexer()))
    # asyncio.run(server.run_server())
    lexer = Lexer()
    parser = Parser(
        lexer.analyze("GET \"slave\";")
    )
    executor = Executor(parser.parse(), Storage(), get_type_router_injector())
    executor.execute()
