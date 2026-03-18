from sqlalchemy.orm import Session
from app.schemas.usuario_schema import Usuario  # Tu modelo de SQLAlchemy
from app.core.security import hash_password # Tu nueva herramienta de seguridad
from app.schemas.usuario_schema import UsuarioCreate

def crear_nuevo_usuario(db: Session, usuario_data: UsuarioCreate):
    # 1. Verificar si el correo ya está registrado
    usuario_existente = db.query(Usuario).filter(Usuario.correo == usuario_data.correo).first()
    
    if usuario_existente:
        return None # O lanzar una excepción de FastAPI

    # 2. Crear la instancia del Modelo con la contraseña ENCRIPTADA
    nuevo_usuario = Usuario(
        nombre=usuario_data.nombre,
        correo=usuario_data.correo,
        rol=usuario_data.rol,
        contrasena=hash_password(usuario_data.contrasena) # <--- AQUÍ ESTÁ LA MAGIA
    )

    # 3. Guardar en MySQL
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario