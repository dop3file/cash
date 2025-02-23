import asyncio

from cash.database import Cash
from cash.parser import Parser
from cash.server import Server
from cash.storage import Storage


async def main():
    server = Server(host="0.0.0.0", port=9092, cash=Cash(Parser(), Storage()))
    await server.run_server()


if __name__ == "__main__":
    asyncio.run(main())
