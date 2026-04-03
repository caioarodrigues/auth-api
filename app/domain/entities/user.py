from dataclasses import dataclass
from typing import Optional
from pydantic import EmailStr


@dataclass
class User:
    name: str
    last_name: str
    email: EmailStr
    password: str
    id: Optional[int] = None