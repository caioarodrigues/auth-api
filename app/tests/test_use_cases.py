from app.use_cases.register_user import RegisterUserUseCase
from app.use_cases.login_user import LoginUserUseCase
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.dtos.user_dto import UserCreateDTO
from app.dtos.auth_dto import LoginDTO


def test_register_user_use_case():

    repo = UserRepositoryImpl()
    use_case = RegisterUserUseCase(repo)

    dto = UserCreateDTO(
        name="UseCase",
        last_name="Test",
        email="usecase@email.com",
        password="12345678"
    )

    user = use_case.execute(dto)

    assert user.id is not None
    assert user.email == "usecase@email.com"


def test_login_user_use_case():

    repo = UserRepositoryImpl()

    register = RegisterUserUseCase(repo)
    login = LoginUserUseCase(repo)

    register.execute(
        UserCreateDTO(
            name="UseCase",
            last_name="Test",
            email="login123@email.com",
            password="12345678"
        )
    )

    token = login.execute(
        LoginDTO(
            email="login123@email.com",
            password="12345678"
        )
    )

    assert isinstance(token, str)


def test_login_invalid_credentials():

    repo = UserRepositoryImpl()

    login = LoginUserUseCase(repo)

    dto = LoginDTO(
        email="invalid@email.com",
        password="wrong"
    )

    try:
        login.execute(dto)
        assert False
    except ValueError:
        assert True