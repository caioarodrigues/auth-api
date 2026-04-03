from fastapi import APIRouter, HTTPException
from app.services.auth_service import AuthService
from app.mappers.user_mapper import UserMapper

router = APIRouter()

auth_service = AuthService()


@router.get("/list-users")
def list_users():
    try:
        users = auth_service.list_users()
        return [UserMapper.to_dto(user) for user in users]
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

