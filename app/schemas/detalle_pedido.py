from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class DetallePedido(Base):
    __tablename__ = "detalle_pedido"

    idDetalle = Column(Integer, primary_key=True, index=True)

    pedido_id = Column(Integer, ForeignKey("pedidos.idPedido"))
    producto_id = Column(Integer, ForeignKey("productos.idProducto"))

    cantidad = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)

    # Relaciones
    producto = relationship("Productos", back_populates="detalle_pedido")




    