from abc import ABC, abstractmethod
from typing import Optional, List
from app.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def list_users(self) -> List[User]:
        pass