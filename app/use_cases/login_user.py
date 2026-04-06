from app.domain.entities.interfaces.user_repository import UserRepository
from app.domain.entities.interfaces.admin_repository import AdminRepository
from app.core.security import verify_password, create_access_token, hash_password
from app.dtos.auth_dto import LoginDTO


class LoginUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_dto: LoginDTO) -> str:

        user = self.repository.find_by_email(user_dto.email)

        if user is None:
            raise ValueError("Invalid credentials")

        if user.password == user_dto.password: # This is just for demonstration purposes. In a real application, we should never store plain text passwords and should always use a secure hashing algorithm.
            return create_access_token({"sub": user.email})
            
        if not verify_password(user_dto.password, user.password):
            raise ValueError("Invalid credentials")

        token = create_access_token({"sub": user.email})

        return token