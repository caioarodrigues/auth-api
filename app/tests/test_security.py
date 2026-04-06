from app.core.security import hash_password, verify_password


def test_password_hashing():
    password = "12345678"

    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_password_verification():
    password = "12345678"

    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_password_verification_wrong_password():
    password = "12345678"
    wrong_password = "wrongpassword"

    hashed = hash_password(password)

    assert verify_password(wrong_password, hashed) is False