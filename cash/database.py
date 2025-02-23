from loguru import logger

from cash.exceptions import CashError
from cash.misc import CashResult
from cash.parser import Parser
from cash.storage import BaseStorage


class Cash:
    def __init__(self, parser: Parser, storage: BaseStorage):
        self._parser = parser
        self._storage = storage

    async def execute_query(self, query: str):
        try:
            operator = self._parser.parse(query)
            result = operator.execute(self._storage)
        except CashError as e:
            return CashResult(error=str(e))
        except Exception as e:
            return CashResult(error="Server error.")
        return CashResult(result=result.to_python())
