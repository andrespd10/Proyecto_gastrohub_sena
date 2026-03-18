from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers import usuarios_controller
from app.core.database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.post("/")
def crear_usuario(nombre:str, correo:str, contrasena:str, rol:str, db:Session = Depends(get_db)):
    return usuarios_controller.crear_usuario(nombre, correo, contrasena, rol, db)

@router.get("/")
def listar_usuarios(db:Session = Depends(get_db)):
    return usuarios_controller.listar_usuarios(db)

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id:int, db:Session = Depends(get_db)):
    return usuarios_controller.obtener_usuario(usuario_id, db)