from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers import productos_controller
from app.core.database import get_db

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post("/")
def crear_producto(nombre:str, descripcion:str, precio:float, db:Session = Depends(get_db)):
    return productos_controller.crear_producto(nombre, descripcion, precio, db)

@router.get("/")
def listar_productos(db:Session = Depends(get_db)):
    return productos_controller.listar_productos(db)

@router.get("/{producto_id}")
def obtener_producto(producto_id:int, db:Session = Depends(get_db)):
    return productos_controller.obtener_producto(producto_id, db)