from dataclasses import dataclass
from app.domain.entities.user import User

@dataclass
class Admin(User):
    type: str = "admin"