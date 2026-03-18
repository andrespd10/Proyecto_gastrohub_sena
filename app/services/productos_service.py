from sqlalchemy.orm import Session
from app.schemas.productos import Productos


def crear_producto(nombre, descripcion, precio, db: Session):

    producto = Productos(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio
    )

    db.add(producto)
    db.commit()
    db.refresh(producto)

    return producto


def listar_productos(db: Session):

    return db.query(Productos).all()


def obtener_producto(producto_id, db: Session):

    return db.query(Productos).filter(Productos.idProducto == producto_id).first()