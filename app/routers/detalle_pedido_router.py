from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers import detalle_pedido_controller
from app.core.database import get_db

router = APIRouter(
    prefix="/detalle-pedido",
    tags=["Detalle Pedido"]
)

@router.post("/")
def agregar_producto(pedido_id:int, producto_id:int, cantidad:int, db:Session = Depends(get_db)):
    return detalle_pedido_controller.agregar_producto(pedido_id, producto_id, cantidad, db)

@router.get("/pedido/{pedido_id}")
def ver_detalle_pedido(pedido_id:int, db:Session = Depends(get_db)):
    return detalle_pedido_controller.ver_detalle_pedido(pedido_id, db)

@router.delete("/{detalle_id}")
def eliminar_producto(detalle_id:int, db:Session = Depends(get_db)):
    return detalle_pedido_controller.eliminar_producto(detalle_id, db)