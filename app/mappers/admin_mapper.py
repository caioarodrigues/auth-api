from app.domain.entities.admin import Admin
from app.dtos.admin_dto import AdminResponseDTO


class AdminMapper:

    @staticmethod
    def to_dto(admin: Admin) -> AdminResponseDTO:
        if not admin.id:
            raise ValueError("Admin ID is required for mapping to DTO")
        if admin is None:
            raise ValueError("Admin entity is required for mapping to DTO")

        return AdminResponseDTO(
            id=admin.id,
            email=admin.email,
            last_name=admin.last_name,
            name=admin.name
        )