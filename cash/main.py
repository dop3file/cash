import asyncio

from cash.config import Config
from cash.core.database import Cash
from cash.core.parser import Parser
from cash.adapters.server import Server
from cash.core.storage import Storage


async def main():
    cash = Cash(Parser(), Storage())
    asyncio.create_task(cash.ttl_observer())
    server = Server(host=Config.HOST, port=Config.PORT, cash=cash)
    await server.run_server()


if __name__ == "__main__":
    asyncio.run(main())
