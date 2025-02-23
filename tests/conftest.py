import asyncio
import json

import pytest
import pytest_asyncio
from loguru import logger

from cash.database import Cash
from cash.parser import Parser
from cash.server import Server
from cash.storage import Storage


class Client:
    MESSAGE_LENGTH = 256
    ENCODING = "utf-8"

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def send_request(self, request: str) -> dict:
        """Отправляет запрос на сервер и возвращает ответ."""
        reader, writer = await asyncio.open_connection(
            self.host,
            self.port
        )

        writer.write(request.encode(self.ENCODING))
        await writer.drain()

        response_data = await reader.read(self.MESSAGE_LENGTH)
        response = json.loads(response_data.decode(self.ENCODING))

        logger.debug(f"Response: {response}")

        writer.close()
        await writer.wait_closed()

        return response

    async def execute_query(self, query_data: dict):
        """Удобный метод для выполнения запроса."""
        return await self.send_request(query_data)


@pytest_asyncio.fixture()
async def client() -> Client:
    return Client(host="0.0.0.0", port=9092)


@pytest.fixture()
def parser():
    return Parser()