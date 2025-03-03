from cash_cli.client import Client
from rich import print


class CashCLI:
    def __init__(self, client: Client) -> None:
        self._client = client

    async def run(self) -> None:
        while True:
            query = input("> ")
            if query in {"EXIT", "exit", "q"}:
                break
            else:
                response = await self._client.send_request(query)
                print(
                    response.error or
                    response.result or
                    response.message or
                    "[bold green]OK.[/bold green]"
                )