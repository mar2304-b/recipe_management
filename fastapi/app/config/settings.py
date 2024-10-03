from dotenv import load_dotenv
import os

load_dotenv()


ENV = os.getenv(
    "ENV", "dev"
    
)

if ENV == "production":
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
        "engine": "peewee.MySQLDatabase",
        "user": os.getenv("MYSQL_USER"), 
        "password": os.getenv("MYSQL_PASSWORD"),
        "host": os.getenv("MYSQL_HOST"),
        "port": int(os.getenv("MYSQL_PORT")),
    }
else:
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
        "engine": "peewee.MySQLDatabase",
        "user": os.getenv("MYSQL_USER"), 
        "password": os.getenv("MYSQL_PASSWORD"),
        "host": os.getenv("MYSQL_HOST"),
        "port": int(os.getenv("MYSQL_PORT")),
    }