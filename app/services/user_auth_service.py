from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.use_cases.login_user import LoginUserUseCase
from app.use_cases.register_user import RegisterUserUseCase
from app.use_cases.list_users import ListUsersUseCase
from app.dtos.user_dto import UserCreateDTO
from app.dtos.auth_dto import LoginDTO


class UserAuthService:

    def __init__(self):

        self.repository = UserRepositoryImpl()

        self.register_use_case = RegisterUserUseCase(self.repository)
        self.login_use_case = LoginUserUseCase(self.repository)
        self.list_users_use_case = ListUsersUseCase(self.repository)

    def register(self, dto: UserCreateDTO):
        return self.register_use_case.execute(dto)

    def login(self, dto: LoginDTO):
        return self.login_use_case.execute(dto)
    
    def list_users(self):
        return self.list_users_use_case.execute()