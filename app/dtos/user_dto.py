from pydantic import BaseModel, EmailStr

class UserCreateDTO(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str


class UserResponseDTO(BaseModel):
    name: str
    last_name: str
    id: int
    email: EmailStr