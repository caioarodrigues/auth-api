from app.infrastructure.repositories.admin_repository_impl import AdminRepositoryImpl
from app.use_cases.login_user import LoginUserUseCase
from app.use_cases.register_user import RegisterUserUseCase
from app.use_cases.list_users import ListUsersUseCase
from app.use_cases.list_admins import ListAdminsUseCase
from app.dtos.user_dto import UserCreateDTO
from app.dtos.admin_dto import AdminCreateDTO
from app.dtos.auth_dto import LoginDTO
from app.domain.entities.user import User


class AdminAuthService:

    def __init__(self):

        self.repository = AdminRepositoryImpl()

        self.login_use_case = LoginUserUseCase(self.repository)
        self.list_users_use_case = ListUsersUseCase(self.repository)
        self.list_admins_use_case = ListAdminsUseCase(self.repository)

    def login(self, dto: LoginDTO):
        return self.login_use_case.execute(dto)
    
    def list_users(self):
        return self.list_users_use_case.execute()
    
    def list_admins(self):
        return self.list_admins_use_case.execute()
      
    def find_admin_by_email(self, email: str):
        return self.repository.find_admin_by_email(email)
    
    def delete_user_by_email(self, email: str):
        return self.repository.delete_user_by_email(email)
    
    def delete_user_by_id(self, user_id: int):
        return self.repository.delete_user_by_id(user_id)
      
    def update_user(self, id: int, user: User):
        return self.repository.update_user(id, user)