from dataclasses import dataclass
from typing import Optional, TypeAlias


Data: TypeAlias = str | bytes | memoryview


@dataclass
class Record:
    data: Data
    ttl: Optional[int]
    last_usage: int
    created_at: int
