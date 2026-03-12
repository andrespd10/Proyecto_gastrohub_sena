from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

# 1. Buscamos el archivo .env en la raíz y cargamos sus valores en memoria
load_dotenv()

class Settings(BaseSettings):
    # Definimos los valores que esperamos leer
    PROJECT_NAME: str = "GastroHub - API"
    
    # Datos de MySQL (los saca del .env)
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")

    # 2. Armamos la URL de conexión que SQLAlchemy necesita
    # Formato: mysql+pymysql://usuario:password@host:puerto/nombre_db
    DATABASE_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    # Configuración de Seguridad
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"

# Creamos una instancia única para usarla en todo el proyecto
settings = Settings()