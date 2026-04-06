from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.domain.entities.user import User
from app.domain.entities.admin import Admin
from app.infrastructure.repositories.admin_repository_impl import AdminRepositoryImpl

def test_create_user_repository():
    repo = UserRepositoryImpl()

    user = User(
        id=None,
        last_name="Test",
        name="Repo",
        email="repo@email.com",
        password="hashedpassword"
    )

    created_user = repo.create(user)

    assert created_user.id is not None
    assert created_user.email == "repo@email.com"


def test_find_user_by_email():
    repo = UserRepositoryImpl()

    user = User(
        last_name="Find",
        name="Repo",
        id=None,
        email="find@email.com",
        password="hash"
    )

    repo.create(user)

    found_user = repo.find_by_email("find@email.com")

    assert found_user is not None
    assert found_user.email == "find@email.com"
    
def test_create_admin_repository():
    repo = AdminRepositoryImpl()

    admin = Admin(
      id=None,
      last_name="Test",
      name="Admin",
      email="admin@email.com",
      password="hashedpassword"
    )
    created_admin = repo.create(admin)
    assert created_admin.id is not None
    assert created_admin.email == "admin@email.com"

def test_find_admin_by_email():
    repo = AdminRepositoryImpl()
    admin = Admin(
      last_name="Find",
      name="Admin",
      id=None,
      email="findadmin@email.com",
      password="hash"
    )
    repo.create(admin)
    found_admin = repo.find_admin_by_email("findadmin@email.com")
    assert found_admin is not None
    assert found_admin.email == "findadmin@email.com"