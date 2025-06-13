"""Pruebas para el login."""


async def test_login_success(client, registered_user):
    """Caso: Inicio de sesión.

    Debe autenticar un usuario registrado y retornar un token válido.
    """
    response = await client.post("/auth/login", json=registered_user)
    assert response.status_code == 200
    body = response.json()

    assert "access_token" in body
    assert body["token_type"] == "bearer"


async def test_login_invalid_credentials(client, registered_user):
    """Caso: Login incorrecto.

    Debe retornar 401 si las credenciales son incorrectas.
    """
    wrong_data = registered_user.copy()
    wrong_data["password"] = "wrongpassword"
    response = await client.post("/auth/login", json=wrong_data)

    assert response.status_code == 401
    assert response.json()["detail"] == "incorrect_credentials"
