"""Pruebas para el registro de usuarios."""


async def test_register_success(client):
    """Caso: Verifica un registro exitoso."""
    payload = {"email": "register@example.com", "password": "test1234"}
    response = await client.post("/auth/register", json=payload)

    assert response.status_code == 200
    assert response.json()["email"] == payload["email"]


async def test_register_existing_user(client, registered_user):
    """Caso: Registrar un usuario ya existente.

    Se hace una primera solicitud de registro, luego otra con los mismos datos.
    """
    response = await client.post("/auth/register", json=registered_user)

    assert response.status_code == 400
    assert response.json()["detail"] == "user_exist"


async def test_register_invalid_email(client):
    """Caso: Correo inválido en el registro.

    Se espera que falle la validación de datos (HTTP 422).
    """
    payload = {"email": "not-an-email", "password": "test123"}
    response = await client.post("/auth/register", json=payload)

    assert response.status_code == 422
