from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers import pedidos_controller
from app.core.database import get_db

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.post("/")
def crear_pedido(mesa_id:int, usuario_id:int, db:Session = Depends(get_db)):
    return pedidos_controller.crear_pedido(mesa_id, usuario_id, db)

@router.get("/")
def listar_pedidos(db:Session = Depends(get_db)):
    return pedidos_controller.listar_pedidos(db)

@router.get("/{pedido_id}")
def obtener_pedido(pedido_id:int, db:Session = Depends(get_db)):
    return pedidos_controller.obtener_pedido(pedido_id, db)

@router.put("/{pedido_id}/estado")
def cambiar_estado(pedido_id:int, estado:str, db:Session = Depends(get_db)):
    return pedidos_controller.cambiar_estado(pedido_id, estado, db)