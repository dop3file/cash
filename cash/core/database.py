import asyncio

from loguru import logger

from cash.config import Config
from cash.core.exceptions import CashError
from cash.core.data_types import CashResult
from cash.core.parser import Parser
from cash.core.storage import IStorage


class Cash:
    def __init__(self, parser: Parser, storage: IStorage):
        self._parser = parser
        self._storage = storage

    async def execute_query(self, query: str):
        try:
            operator = self._parser.parse(query)
            result = operator.execute(self._storage)
        except CashError as e:
            return CashResult(error=str(e))
        except Exception as e:
            logger.error(e)
            return CashResult(error="Server error.")
        return CashResult(result=result.to_python(), message=result.get_message())

    async def ttl_observer(self) -> None:
        while True:
            for value in self._storage.values():
                logger.debug(value)
                if value.is_expired():
                    self._storage.delete(value.key)

            await asyncio.sleep(Config.TTL_DELAY_CHECK)
