from typing import List
from app.domain.entities.user import User
from app.domain.entities.admin import Admin

admin_mock_1 = Admin(id=1, email="admin@example.com", password="hashed_password", type="admin", name="Admin User", last_name="Test")
admin_mock_2 = Admin(id=2, email="admin2@example.com", password="hashed_password", type="admin", name="Admin", last_name="User2")
admin_mock_3 = Admin(id=3, email="admin3@example.com", password="hashed_password", type="admin", name="Admin", last_name="User3")
admin_mock_4 = Admin(id=4, email="admin4@example.com", password="hashed_password", type="admin", name="Admin", last_name="User4")
admin_mock_5 = Admin(id=5, email="admin5@example.com", password="hashed_password", type="admin", name="Admin", last_name="User5")
admin_mock_6 = Admin(id=6, email="admin6@example.com", password="hashed_password", type="admin", name="Admin", last_name="User6")

user_mock_1 = User(id=7, email="user1@example.com", password="hashed_password", type="user", name="John", last_name="Doe")
user_mock_2 = User(id=8, email="user2@example.com", password="hashed_password", type="user", name="Jane", last_name="Smith")
user_mock_3 = User(id=9, email="user3@example.com", password="hashed_password", type="user", name="Carlos", last_name="Silva")
user_mock_4 = User(id=10, email="user4@example.com", password="hashed_password", type="user", name="Maria", last_name="Santos")
user_mock_5 = User(id=11, email="user5@example.com", password="hashed_password", type="user", name="Pedro", last_name="Oliveira")

fake_db: List[User | Admin] = [admin_mock_1, admin_mock_2, admin_mock_3, admin_mock_4, admin_mock_5, admin_mock_6, user_mock_1, user_mock_2, user_mock_3, user_mock_4, user_mock_5]