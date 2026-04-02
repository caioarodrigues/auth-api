from fastapi import APIRouter, HTTPException
from app.services.auth_service import AuthService
from app.dtos.user_dto import UserCreateDTO
from app.dtos.auth_dto import LoginDTO, TokenDTO
from app.mappers.user_mapper import UserMapper

router = APIRouter()

auth_service = AuthService()


@router.post("/register")
def register(dto: UserCreateDTO):
    try:
        user = auth_service.register(dto)

        return UserMapper.to_dto(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenDTO)
def login(dto: LoginDTO):

    try:
        token = auth_service.login(dto)
        return TokenDTO(access_token=token)

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")