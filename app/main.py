from fastapi import FastAPI
from app.core.database import engine, Base
from .models import user_model # Importamos el modelo para que SQLAlchemy lo reconozca

# Esta línea es la "orden de construcción"
# Mira todos los modelos que heredan de 'Base' y crea las tablas en MySQL si no existen
Base.metadata.create_all(bind=engine)

# Creamos la instancia de la aplicación
app = FastAPI(title="GastroHub - API")

# Una ruta de bienvenida para probar en el navegador
@app.get("/")
def home():
    return {"Mensaje": "Bienvenido a la API de GastroHub", "Estado": "Conexión Exitosa"}