from dataclasses import dataclass, field


@dataclass
class CashResult:
    error: str | None = None
    result: str | None = None
