import asyncio
from dataclasses import asdict

from loguru import logger
import orjson as json

from cash.core.database import Cash


class Server:
    MESSAGE_LENGTH = 256
    ENCODING = "utf-8"

    def __init__(self, host: str, port: int, cash: Cash):
        self._host = host
        self._port = port
        self._cash = cash

    async def handle_client(self, reader, writer):
        request = (await reader.read(self.MESSAGE_LENGTH)).decode(self.ENCODING)
        logger.info(f"Request: {request}")
        response = await self._cash.execute_query(request)
        response = asdict(response)
        logger.info(response)
        writer.write(json.dumps(response))
        await writer.drain()
        writer.close()

    async def run_server(self):
        logger.info("Start server")
        server = await asyncio.start_server(self.handle_client, self._host, self._port)
        async with server:
            await server.serve_forever()
