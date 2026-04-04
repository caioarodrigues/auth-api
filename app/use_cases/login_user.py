from app.domain.entities.interfaces.user_repository import UserRepository
from app.domain.entities.interfaces.admin_repository import AdminRepository
from app.core.security import verify_password, create_access_token
from app.dtos.auth_dto import LoginDTO


class LoginUserUseCase:

    def __init__(self, repository: UserRepository | AdminRepository):
        self.repository = repository

    def execute(self, dto: LoginDTO) -> str:

        user = self.repository.find_admin_by_email(dto.email)

        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(dto.password, user.password):
            raise ValueError("Invalid credentials")

        token = create_access_token({"sub": user.email})

        return token