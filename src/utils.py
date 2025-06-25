import bcrypt

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    if not password:
        raise ValueError("Password cannot be empty")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hashed password."""
    if not plain_password or not hashed_password:
        raise ValueError("Password and hashed password cannot be empty")
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))