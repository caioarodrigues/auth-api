from fastapi import APIRouter, HTTPException
from app.services.user_auth_service import UserAuthService
from app.dtos.user_dto import UserCreateDTO
from app.dtos.auth_dto import LoginDTO, TokenDTO
from app.mappers.user_mapper import UserMapper

router = APIRouter()

auth_service = UserAuthService()


@router.post("/register")
def register_new_user(new_user: UserCreateDTO):
    try:
        user = auth_service.register(new_user)

        return UserMapper.to_dto(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenDTO)
def login(user_login: LoginDTO):

    try:
        token = auth_service.login(user_login)
        return TokenDTO(access_token=token)

    except ValueError as ve:
        raise HTTPException(status_code=401, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))