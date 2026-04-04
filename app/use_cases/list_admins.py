from app.domain.entities.admin import Admin
from app.domain.entities.interfaces.user_repository import UserRepository
from app.domain.entities.interfaces.admin_repository import AdminRepository
from typing import List

class ListAdminsUseCase:

    def __init__(self, repository: AdminRepository):
        self.repository = repository

    def execute(self) -> List[Admin]:
        admins = self.repository.list_admins()

        if not admins:
            raise ValueError("No admins found")
        return admins

            