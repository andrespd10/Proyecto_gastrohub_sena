from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers import mesas_controller
from app.core.database import get_db

router = APIRouter(
    prefix="/mesas",
    tags=["Mesas"]
)

@router.post("/")
def crear_mesa(numeroMesa:int, db:Session = Depends(get_db)):
    return mesas_controller.crear_mesa(numeroMesa, db)

@router.get("/")
def listar_mesas(db:Session = Depends(get_db)):
    return mesas_controller.listar_mesas(db)

@router.get("/{mesa_id}")
def obtener_mesa(mesa_id:int, db:Session = Depends(get_db)):
    return mesas_controller.obtener_mesa(mesa_id, db)