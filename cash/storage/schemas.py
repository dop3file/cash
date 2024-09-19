from dataclasses import dataclass
from typing import Optional

from cash.utils import Value


@dataclass
class Record:
    data: Value
    ttl: Optional[int]
    last_usage: int
    created_at: int
