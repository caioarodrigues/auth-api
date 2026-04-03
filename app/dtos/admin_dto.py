from pydantic import BaseModel, EmailStr

class AdminCreateDTO(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str


class AdminResponseDTO(BaseModel):
    name: str
    last_name: str
    id: int
    email: EmailStr