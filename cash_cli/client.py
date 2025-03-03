import asyncio
from dataclasses import dataclass

import orjson as json
from loguru import logger


@dataclass
class Response:
    error: str
    message: str
    result: str


class Client:
    MESSAGE_LENGTH = 256
    ENCODING = "utf-8"

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def send_request(self, request: str) -> Response:
        reader, writer = await asyncio.open_connection(
            self.host,
            self.port
        )

        writer.write(request.encode(self.ENCODING))
        await writer.drain()

        response_data = await reader.read(self.MESSAGE_LENGTH)
        response = json.loads(response_data.decode(self.ENCODING))

        writer.close()
        await writer.wait_closed()

        return Response(**response)
