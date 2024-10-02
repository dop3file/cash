import asyncio

from loguru import logger
import orjson as json

from cash.database import Database


class Server:
    MESSAGE_LENGTH = 256
    ENCODING = "utf-8"

    def __init__(self, host: str, port: int, database: Database):
        self.host = host
        self.port = port
        self.database = database

    async def handle_client(self, reader, writer):
        request = (await reader.read(self.MESSAGE_LENGTH)).decode(self.ENCODING)
        logger.debug(f"Request: {request}")
        response = await self.database.execute_command(request)
        response = response.dict()
        logger.debug(response)
        writer.write(json.dumps(response))

        await writer.drain()
        writer.close()

    async def run_server(self):
        logger.debug("Start server")
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        async with server:
            await self.database.execute_planning_tasks()
            await server.serve_forever()