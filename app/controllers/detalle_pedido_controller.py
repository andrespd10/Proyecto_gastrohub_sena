from sqlalchemy.orm import Session
from app.services import detalle_pedido_service


def agregar_producto(pedido_id, producto_id, cantidad, db: Session):
    return detalle_pedido_service.agregar_producto(pedido_id, producto_id, cantidad, db)


def ver_detalle_pedido(pedido_id, db: Session):
    return detalle_pedido_service.ver_detalle_pedido(pedido_id, db)


def eliminar_producto(detalle_id, db: Session):
    return detalle_pedido_service.eliminar_producto(detalle_id, db)