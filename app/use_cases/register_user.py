from app.domain.entities.user import User
from app.domain.entities.interfaces.user_repository import UserRepository
from app.core.security import hash_password
from app.dtos.user_dto import UserCreateDTO

class RegisterUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_dto: UserCreateDTO) -> User:

        try:
            hashed_password = hash_password(user_dto.password)
            
            if self.repository.find_by_email(user_dto.email):
                raise Exception("Email already registered")
            
            user = User(
                name=user_dto.name,
                last_name=user_dto.last_name,
                email=user_dto.email,
                password=hashed_password
            )
            
            return self.repository.create(user)
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            raise e