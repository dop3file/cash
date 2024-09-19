from dataclasses import dataclass
from typing import Optional, TypeAlias


@dataclass
class Record:
    data: Data
    ttl: Optional[int]
    last_usage: int
    created_at: int
