def get_token(client):
    client.post(
        "/auth/register",
        json={
            "name": "Protected",
            "last_name": "User",
            "email": "protected@email.com",
            "password": "12345678"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "protected@email.com",
            "password": "12345678"
        }
    )

    return response.json()["access_token"]


def test_protected_route_requires_token(client):
    response = client.get("/admin/list-users")

    assert response.status_code == 401


def test_protected_route_with_token(client):
    token = get_token(client)

    response = client.get(
        "/admin/list-users",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200