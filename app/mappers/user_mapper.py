from app.domain.entities.user import User
from app.dtos.user_dto import UserResponseDTO


class UserMapper:

    @staticmethod
    def to_dto(user: User) -> UserResponseDTO:
        return UserResponseDTO(
            id=user.id,
            email=user.email
        )