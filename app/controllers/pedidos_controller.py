from sqlalchemy.orm import Session
from app.services import pedidos_service


def crear_pedido(mesa_id, usuario_id, db: Session):
    return pedidos_service.crear_pedido(mesa_id, usuario_id, db)


def listar_pedidos(db: Session):
    return pedidos_service.listar_pedidos(db)


def obtener_pedido(pedido_id, db: Session):
    return pedidos_service.obtener_pedido(pedido_id, db)


def cambiar_estado(pedido_id, estado, db: Session):
    return pedidos_service.cambiar_estado(pedido_id, estado, db)