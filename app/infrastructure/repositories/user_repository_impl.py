from typing import Optional
from app.domain.entities.user import User
from app.domain.entities.interfaces.user_repository import UserRepository
from app.infrastructure.database import fake_db


class UserRepositoryImpl(UserRepository):

    def create(self, user: User) -> User:

        user.id = len(fake_db) + 1
        fake_db.append(user)

        return user

    def find_by_email(self, email: str) -> Optional[User]:

        for user in fake_db:
            if user.email == email:
                return user

        return None