from jose import jwt
from app.core.security import create_access_token
from app.core.config import settings


def test_create_access_token():
    token = create_access_token({"sub": "test@email.com"})

    assert isinstance(token, str)


def test_decode_token():
    token = create_access_token({"sub": "user@email.com"})

    payload = jwt.decode(
        token,
        settings.jwt_secret,
        algorithms=[settings.jwt_algorithm],
    )

    assert payload["sub"] == "user@email.com"