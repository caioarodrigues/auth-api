from pydantic import BaseModel, EmailStr


class UserCreateDTO(BaseModel):
    email: EmailStr
    password: str


class UserResponseDTO(BaseModel):
    id: int | None
    email: EmailStr