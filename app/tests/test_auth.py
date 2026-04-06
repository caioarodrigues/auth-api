def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "name": "Maria",
            "last_name": "Andrade",
            "email": "test@email.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()

    assert data["email"] == "test@email.com", "Expected to receive an email "
    assert "id" in data, "Expected to receive an id"

def test_register_user_existing_email(client):
    response = client.post(
        "/auth/register",
        json={
            "name": "Maria",
            "last_name": "Andrade",
            "email": "admin@example.com",
            "password": "12345678"
        }   
      )
    assert response.status_code == 400, "Expected status code 400, got {response.status_code}"
    data = response.json()
    assert data["detail"] == "Email already registered", "Expected error message 'Email already registered', got {data['detail']}"
    
def test_login_existing_user(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "admin@example.com",
            "password": "hashed_password"
        }
    )
    
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert "access_token" in data, "Expected 'access_token' in response, got {data}"
    

def test_register_and_login_user(client):
    client.post(
        "/auth/register",
        json={
            "name": "João",
            "last_name": "Silva",
            "email": "login@email.com",
            "password": "12345678"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "login@email.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert "access_token" in data

def test_login_user_invalid_credentials(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "invalid@email.com",
            "password": "invalidpassword"
        }
    )

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Invalid credentials"

def test_login_user_wrong_password(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "admin@example.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401, "Expected status code 401, got {response.status_code}"
    data = response.json()
    assert data["detail"] == "hash could not be identified", "Expected error message 'hash could not be identified', got {data['detail']}"