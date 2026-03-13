from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Pedidos(Base):
    __tablename__ = "pedidos"

    idPedido = Column(Integer, primary_key=True, index=True)

    mesa_id = Column(Integer, ForeignKey("mesas.idMesa"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.idUsuario"), nullable=False)

    estado = Column(String(20), default="pendiente")  # pendiente, preparando, listo, pagado
    fecha = Column(DateTime, default=datetime.utcnow)

    total = Column(Float, default=0)

    # Relaciones
    mesa = relationship("Mesas", back_populates="pedidos")
    usuario = relationship("Usuarios")
    detalles = relationship("DetallePedido", back_populates="pedido")
    pago = relationship("Pagos", back_populates="pedido", uselist=False)