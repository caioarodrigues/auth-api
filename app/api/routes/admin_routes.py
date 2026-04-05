from fastapi import APIRouter, HTTPException, Depends
from app.services.user_auth_service import UserAuthService
from app.mappers.user_mapper import UserMapper
from app.mappers.admin_mapper import AdminMapper
from app.services.admin_auth_service import AdminAuthService
from app.domain.entities.user import User
from app.core.dependencies.auth_dependency import get_current_user

router = APIRouter()

auth_service = UserAuthService()
admin_auth_service = AdminAuthService()


@router.get("/list-users")
def list_users(current_email: str = Depends(get_current_user)):
    try:
        users = auth_service.list_users()
        return [UserMapper.to_dto(user) for user in users]
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/list-admins")
def list_admins(current_email: str = Depends(get_current_user)):
    try:
        valid_email = admin_auth_service.find_admin_by_email(current_email)
        
        if valid_email is None:
            raise ValueError("You do not have permission for this action")

        admins = admin_auth_service.list_admins()
        return [AdminMapper.to_dto(admin) for admin in admins]
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/find-admin-by-email")
def find_admin_by_email(email: str, current_email: str = Depends(get_current_user)):
    try:
        admin = admin_auth_service.find_admin_by_email(email)
        if admin is None:
            raise ValueError("Admin not found")
        else:
            return AdminMapper.to_dto(admin)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/user/delete/id={user_id}")
def delete_user_by_id(user_id: int, current_email: str = Depends(get_current_user)):
    try:
        user = admin_auth_service.delete_user_by_id(user_id)
        return UserMapper.to_dto(user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/user/delete/email={email}")
def delete_user_by_email(email: str, current_email: str = Depends(get_current_user)):
    try:
        user = admin_auth_service.delete_user_by_email(email)
        return UserMapper.to_dto(user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/user/update/id={user_id}")
def update_user(user_id: int, name: str, last_name: str, email: str, password: str, current_email: str = Depends(get_current_user)):
    try:
        user = admin_auth_service.update_user(user_id, User(id=user_id, name=name, last_name=last_name, email=email, password=password, type='user'))
        return UserMapper.to_dto(user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 