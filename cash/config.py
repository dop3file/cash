from dataclasses import dataclass
from typing import Literal

from envparse import env


@dataclass
class Config:
    HOST = env("CASH_HOST", default="0.0.0.0")
    PORT = env.int("CASH_PORT", default=9091)
    PERSISTENCE_MODE: Literal["SNAPSHOT", "AOF", "NOTHING"] = env(
        "CASH_PERSISTENCE_LEVEL", default="NOTHING"
    )
    SNAPSHOT_DELAY: int = env.int("CASH_SNAPSHOT_DELAY", default=5)
    AOF_ROTATION_SIZE: str = env("CASH_AOF_ROTATION_SIZE", default="5Mb")
    AOF_DELAY: int = env.int("CASH_AOF_DELAY", default=1)
    TTL_DELAY_CHECK: int = env.int("CASH_TTL_DELAY_CHECK", default=1)
