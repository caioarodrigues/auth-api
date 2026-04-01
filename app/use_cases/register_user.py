from app.domain.entities.user import User
from app.domain.entities.interfaces.user_repository import UserRepository
from app.core.security import hash_password
from app.dtos.user_dto import UserCreateDTO

class RegisterUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, dto: UserCreateDTO) -> User:

        try:
            hashed_password = hash_password(dto.password)

            user = User(
                id=None,
                email=dto.email,
                password=hashed_password
            )

            return self.repository.create(user)
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            raise e