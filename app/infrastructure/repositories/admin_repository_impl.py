from typing import Optional, List
from app.domain.entities.admin import Admin
from app.domain.entities.interfaces.admin_repository import AdminRepository
from app.domain.entities.user import User
from app.infrastructure.database import fake_db


class AdminRepositoryImpl(AdminRepository):
    
    def create(self, admin: Admin) -> Admin:

        admin.id = len(fake_db) + 1
        fake_db.append(admin)

        return admin

    def find_admin_by_email(self, email: str) -> Optional[Admin]:

        try:
            for item in fake_db:
                if item.email == email and item.type == "admin" and isinstance(item, Admin):
                    return item
            else:
                raise ValueError("Admin not found")
        except Exception as e:
            raise e

    def list_admins(self) -> List[Admin]:
        admins = [item for item in fake_db if isinstance(item, Admin) and item.type == 'admin']
        return admins
    
    def list_users(self) -> List[User]:
        raise NotImplementedError

    def delete_user_by_email(self, email: str) -> User:
        for item in fake_db:
            if item.email == email and isinstance(item, User) and item.type == 'user':
                fake_db.remove(item)
                return item
        
        raise ValueError("User not found")
    def delete_user_by_id(self, user_id: int) -> User:
        for item in fake_db:
            if item.id == user_id and isinstance(item, User) and item.type == 'user':
                fake_db.remove(item)
                return item
        
        raise ValueError("User not found")

    def update_user(self, id: int, user: User) -> User | Admin:
        for item in fake_db:
            if item.id == id and isinstance(item, User) and item.type == 'user':
                fake_db.remove(item)
                fake_db.append(user)
                return user
        
        raise ValueError("User not found")
