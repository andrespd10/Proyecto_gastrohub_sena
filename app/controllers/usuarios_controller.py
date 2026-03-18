from sqlalchemy.orm import Session
from app.services import usuarios_service


def crear_usuario(nombre, correo, contrasena, rol, db: Session):
    return usuarios_service.crear_usuario(nombre, correo, contrasena, rol, db)


def listar_usuarios(db: Session):
    return usuarios_service.listar_usuarios(db)


def obtener_usuario(usuario_id, db: Session):
    return usuarios_service.obtener_usuario(usuario_id, db)