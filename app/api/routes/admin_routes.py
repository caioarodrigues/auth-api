from fastapi import APIRouter, HTTPException
from app.services.auth_service import AuthService
from app.mappers.user_mapper import UserMapper

router = APIRouter()

auth_service = AuthService()


@router.get("/list-users")
def list_users():
    users = auth_service.list_users()
    
    if len(users) == 0:
        raise HTTPException(status_code=404, detail="No users found")

    return [UserMapper.to_dto(user) for user in users]
