from dataclasses import dataclass
from typing import Literal

from envparse import env


@dataclass
class Config:
    HOST = env("host")
    PORT = env("port")
    PERSISTENCE_LEVEL: Literal["SNAPSHOT", "LOG", "NOTHING"] = env(
        "PERSISTENCE_LEVEL", default="NOTHING"
    )
    SNAPSHOT_DELAY: int = env("SNAPSHOT_DELAY", default=5)

