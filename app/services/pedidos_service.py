from sqlalchemy.orm import Session
from app.schemas.pedido import Pedidos
from app.schemas.mesa import Mesas


def crear_pedido(mesa_id, usuario_id, db: Session):

    mesa = db.query(Mesas).filter(Mesas.idMesa == mesa_id).first()

    if not mesa:
        return {"error": "Mesa no existe"}

    if mesa.estado == "ocupada":
        return {"error": "Mesa ocupada"}

    mesa.estado = "ocupada"

    pedido = Pedidos(
        mesa_id=mesa_id,
        usuario_id=usuario_id,
        estado="pendiente",
        total=0
    )

    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    return pedido


def listar_pedidos(db: Session):

    return db.query(Pedidos).all()


def obtener_pedido(pedido_id, db: Session):

    return db.query(Pedidos).filter(Pedidos.idPedido == pedido_id).first()


def cambiar_estado(pedido_id, estado, db: Session):

    pedido = db.query(Pedidos).filter(Pedidos.idPedido == pedido_id).first()

    if not pedido:
        return {"error": "Pedido no encontrado"}

    pedido.estado = estado

    db.commit()

    return pedido