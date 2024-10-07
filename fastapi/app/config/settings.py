from dotenv import load_dotenv  # Importa la función para cargar variables de entorno
import os  # Importa el módulo para interactuar con el sistema operativo

load_dotenv()  # Carga las variables de entorno desde el archivo .env

# Carga el entorno (por defecto "dev").
ENV = os.getenv("ENV", "dev")

# Configuración de la base de datos según el entorno.
if ENV == "production":
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),  # Nombre de la base de datos
        "engine": "peewee.MySQLDatabase",  # Motor de la base de datos
        "user": os.getenv("MYSQL_USER"),  # Usuario de la base de datos
        "password": os.getenv("MYSQL_PASSWORD"),  # Contraseña del usuario
        "host": os.getenv("MYSQL_HOST"),  # Host de la base de datos
        "port": int(os.getenv("MYSQL_PORT")),  # Puerto de conexión
    }
else:
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),  # Nombre de la base de datos
        "engine": "peewee.MySQLDatabase",  # Motor de la base de datos
        "user": os.getenv("MYSQL_USER"),  # Usuario de la base de datos
        "password": os.getenv("MYSQL_PASSWORD"),  # Contraseña del usuario
        "host": os.getenv("MYSQL_HOST"),  # Host de la base de datos
        "port": int(os.getenv("MYSQL_PORT")),  # Puerto de conexión
    }
