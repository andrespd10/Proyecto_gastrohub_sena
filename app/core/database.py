from sqlalchemy import create_engine # El "motor" que se conecta al servidor
from sqlalchemy.ext.declarative import declarative_base # La "madre" de tus tablas
from sqlalchemy.orm import sessionmaker # La "fábrica" para hacer consultas
from app.core.config import settings # Tus credenciales del .env

# 1. Creamos el motor (Engine)
# Es el objeto que mantiene la conexión física con MySQL.
engine = create_engine(settings.DATABASE_URL)

# 2. Creamos la sesión (SessionLocal)
# Cada vez que alguien pida datos, esta fábrica le entregará una sesión.
# autocommit=False: No guarda cambios hasta que tú le digas "commit".
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. La Base para los modelos
# Todas tus clases (Usuario, Pedido, etc.) heredarán de aquí para que 
# SQLAlchemy sepa que deben ser tablas en MySQL.
Base = declarative_base()

# 4. Función de ayuda (Dependencia)
# Esta función abre una conexión y se asegura de cerrarla cuando termine la tarea.
def get_db():
    db = SessionLocal()
    try:
        yield db # Presta la conexión
    finally:
        db.close() # Cierra la conexión SIEMPRE