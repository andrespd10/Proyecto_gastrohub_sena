from passlib.context import CryptContext

# CryptContext es la configuración de hashing.
# schemes=["bcrypt"] indica que usaremos bcrypt (el estándar seguro para contraseñas).
# deprecated="auto" permite que passlib migre hashes antiguos si detecta uno obsoleto.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    - Recibe la contraseña en texto plano (ej: "MiPass123").
    - Devuelve un HASH seguro (ej: "$2b$12$...").
    - Ese hash NO es reversible (no puedes obtener la contraseña original).
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    - Recibe:
    #   - plain_password: contraseña que escribe el usuario.
    #   - hashed_password: hash almacenado en la DB.
    - Devuelve True si coinciden, False si no.
    """
    return pwd_context.verify(plain_password, hashed_password)