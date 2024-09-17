import asyncio

from loguru import logger


class Server:
    MESSAGE_LENGTH = 256
    ENCODING = "utf-8"

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def handle_client(self, reader, writer):
        request = (await reader.read(self.MESSAGE_LENGTH)).decode(self.ENCODING)
        logger.debug(f"Request: {request}")
        response = request
        writer.write(response.encode(self.ENCODING))
        await writer.drain()
        writer.close()

    async def run_server(self):
        logger.debug("Start server")
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        async with server:
            await server.serve_forever()