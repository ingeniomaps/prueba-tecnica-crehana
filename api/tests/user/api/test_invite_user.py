"""Invitación de usuarios."""


async def test_invite_user_success(client, authorization_user):
    """algo."""
    payload = {
        "email": "user@example.com",
        "subject": "Invitación",
        "body": "Has sido invitado.",
    }

    response = await client.post("/user/board/invite", json=payload, headers=authorization_user)

    assert response.status_code == 200
    assert response.json()["code"] == "send_email"
