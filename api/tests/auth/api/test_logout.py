"""Pruebas para el logout."""


async def test_logout(client):
    """Caso: Cerrar sesión."""
    response = await client.post("/auth/logout")

    assert response.status_code == 200
    assert response.json()["detail"] == "logout"
