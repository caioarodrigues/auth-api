from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: Optional[int]
    email: str
    password: str