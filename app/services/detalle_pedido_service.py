from sqlalchemy.orm import Session
from app.schemas.productos import Productos
from app.schemas.pedido import Pedidos
from app.schemas.detalle_pedido import DetallePedido


def agregar_producto(pedido_id, producto_id, cantidad, db: Session):

    producto = db.query(Productos).filter(Productos.idProducto == producto_id).first()

    if not producto:
        return {"error": "Producto no existe"}

    subtotal = producto.precio * cantidad

    detalle = DetallePedido(
        pedido_id=pedido_id,
        producto_id=producto_id,
        cantidad=cantidad,
        subtotal=subtotal
    )

    db.add(detalle)

    pedido = db.query(Pedidos).filter(Pedidos.idPedido == pedido_id).first()

    pedido.total += subtotal

    db.commit()

    return detalle


def ver_detalle_pedido(pedido_id, db: Session):

    return db.query(DetallePedido).filter(DetallePedido.pedido_id == pedido_id).all()


def eliminar_producto(detalle_id, db: Session):

    detalle = db.query(DetallePedido).filter(DetallePedido.idDetalle == detalle_id).first()

    if not detalle:
        return {"error": "Detalle no encontrado"}

    pedido = db.query(Pedidos).filter(Pedidos.idPedido == detalle.pedido_id).first()

    pedido.total -= detalle.subtotal

    db.delete(detalle)

    db.commit()

    return {"mensaje": "Producto eliminado"}