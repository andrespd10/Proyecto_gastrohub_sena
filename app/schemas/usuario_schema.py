from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Usuarios(Base):
    # Nombre de la tabla en MySQL Workbench
    __tablename__ = "usuarios"

    # Traduciendo tu UML a SQLAlchemy:
    idUsuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    contrasena = Column(String(255), nullable=False) # Almacenaremos el HASH
    rol = Column(String(20), nullable=False) # admin, mesero, cocinero
    estado = Column(Boolean, default=True) # True = Activo, False = Desactivado