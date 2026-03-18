from sqlalchemy.orm import Session
from app.schemas.mesa import Mesas


def crear_mesa(numeroMesa, db: Session):

    mesa = Mesas(
        numeroMesa=numeroMesa,
        estado="libre"
    )

    db.add(mesa)
    db.commit()
    db.refresh(mesa)

    return mesa


def listar_mesas(db: Session):

    return db.query(Mesas).all()


def obtener_mesa(mesa_id, db: Session):

    return db.query(Mesas).filter(Mesas.idMesa == mesa_id).first()