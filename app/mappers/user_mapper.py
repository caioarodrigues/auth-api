from app.domain.entities.user import User
from app.dtos.user_dto import UserResponseDTO


class UserMapper:

    @staticmethod
    def to_dto(user: User) -> UserResponseDTO:
        if not user.id:
            raise ValueError("User ID is required for mapping to DTO")

        return UserResponseDTO(
            id=user.id,
            email=user.email,
            last_name=user.last_name,
            name=user.name
        )