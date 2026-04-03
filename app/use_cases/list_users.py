from app.domain.entities.user import User
from app.domain.entities.interfaces.user_repository import UserRepository
from typing import List

class ListUsersUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> List[User]:
        users = self.repository.list_users()

        if not users:
            raise ValueError("No users found")
        return users

            