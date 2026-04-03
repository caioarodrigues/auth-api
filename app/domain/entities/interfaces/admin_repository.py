from abc import ABC, abstractmethod
from typing import Optional, List
from app.domain.entities.user import User
from app.domain.entities.admin import Admin

class AdminRepository(ABC):

    @abstractmethod
    def create(self, admin: Admin) -> Admin:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Admin]:
        pass
    
    @abstractmethod
    def list_admins(self) -> List[Admin]:
        pass
    
    @abstractmethod
    def delete_user_by_email(self, email: str) -> User:
        pass
      
    @abstractmethod
    def delete_user_by_id(self, user_id: int) -> User:
        pass
    
    @abstractmethod
    def update_user(self, email: str, updated_user: User) -> User:
        pass
    