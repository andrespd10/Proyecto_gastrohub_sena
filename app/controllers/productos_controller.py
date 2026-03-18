from sqlalchemy.orm import Session
from app.services import productos_service


def crear_producto(nombre, descripcion, precio, db: Session):
    return productos_service.crear_producto(nombre, descripcion, precio, db)


def listar_productos(db: Session):
    return productos_service.listar_productos(db)


def obtener_producto(producto_id, db: Session):
    return productos_service.obtener_producto(producto_id, db)