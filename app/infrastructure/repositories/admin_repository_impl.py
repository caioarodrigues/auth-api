from typing import Optional, List
from app.domain.entities.admin import Admin
from app.domain.entities.interfaces.admin_repository import AdminRepository
from app.infrastructure.database import fake_db


class AdminRepositoryImpl(AdminRepository):
    
    def create(self, admin: Admin) -> Admin:

        admin.id = len(fake_db) + 1
        fake_db.append(admin)

        return admin

    def find_by_email(self, email: str) -> Optional[Admin]:

        for item in fake_db:
            if item.email == email and item.type == "admin" and isinstance(item, Admin):
                return item

        return None
    
    def list_admins(self) -> List[Admin]:
        return [item for item in fake_db if isinstance(item, Admin)]