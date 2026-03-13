from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Mesas(Base):
    __tablename__ = "mesas"

    idMesa = Column(Integer, primary_key=True, index=True)
    numeroMesa = Column(Integer, unique=True, nullable=False)
    estado = Column(String(20), default="libre")  # libre / ocupada

    # Relación con pedidos
    pedidos = relationship("Pedidos", back_populates="mesa")