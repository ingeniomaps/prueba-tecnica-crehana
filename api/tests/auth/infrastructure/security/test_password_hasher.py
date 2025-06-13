"""Hasheo de contraseñas."""

from app.auth.infrastructure.security.password_hasher import hash_password, verify_password


def test_hash_password_returns_different_value():
    """Caso: Hash diferente a la contraseña original."""
    plain = "password"
    hashed = hash_password(plain)

    assert hashed != plain
    assert isinstance(hashed, str)
    assert hashed.startswith("$argon2")


def test_verify_password_correct():
    """Caso: Contraseña correcta."""
    password = "password"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_verify_password_incorrect():
    """Caso: Contraseña incorrecta."""
    original = "password"
    wrong = "password123"
    hashed = hash_password(original)

    assert verify_password(wrong, hashed) is False
