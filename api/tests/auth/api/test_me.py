"""Pruebas para las rutas de autenticación y usuario."""


async def test_me_returns_authenticated_user(client, registered_user):
    """Caso: Retornar usuario en sesión.

    Debe retornar los datos del usuario autenticado usando el token.
    """
    login_res = await client.post("/auth/login", json=registered_user)
    token = login_res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = await client.get("/auth/me", headers=headers)

    assert response.status_code == 200
    assert response.json()["email"] == registered_user["email"]


async def test_me_without_token_returns_unauthorized(client):
    """Caso: Token invalido.

    Debe retornar 401 si no se envía token.
    """
    response = await client.get("/auth/me")

    assert response.status_code == 401
