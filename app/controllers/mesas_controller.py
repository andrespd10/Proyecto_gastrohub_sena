from sqlalchemy.orm import Session
from app.services import mesas_service


def crear_mesa(numeroMesa, db: Session):
    return mesas_service.crear_mesa(numeroMesa, db)


def listar_mesas(db: Session):
    return mesas_service.listar_mesas(db)


def obtener_mesa(mesa_id, db: Session):
    return mesas_service.obtener_mesa(mesa_id, db)