from fastapi import FastAPI
from app.core.database import engine, Base
from .schemas import productos, mesa, pedido, detalle_pedido, usuario_schema # Importamos el modelo para que SQLAlchemy lo reconozca

# Importamos los routers
from app.routers import usuarios_router
from app.routers import productos_router
from app.routers import mesas_router
from app.routers import pedidos_router
from app.routers import detalle_pedido_router


# Esta línea es la "orden de construcción"
# Mira todos los modelos que heredan de 'Base' y crea las tablas en MySQL si no existen
Base.metadata.create_all(bind=engine)

# Creamos la instancia de la aplicación
app = FastAPI(title="GastroHub - API")


# Registramos los routers para que las rutas definidas en cada uno estén disponibles
app.include_router(usuarios_router.router)
app.include_router(productos_router.router)
app.include_router(mesas_router.router)
app.include_router(pedidos_router.router)
app.include_router(detalle_pedido_router.router)


# Una ruta de bienvenida para probar en el navegador
@app.get("/")
def home():
    return {"Mensaje": "Bienvenido a la API de GastroHub", "Estado": "Conexión Exitosa"}