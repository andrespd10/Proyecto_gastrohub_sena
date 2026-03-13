from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base

class Productos(Base):
    # Nombre de la tabla en MySQL Workbench
    __tablename__ = "productos"

    # Traduciendo tu UML a SQLAlchemy:
    idProducto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Float, nullable=False)
    imagenes = Column(String(255), nullable=True) # URL o ruta de la imagen
    estado = Column(Boolean, default=True) # True = Disponible, False = No Disponible