from dotenv import load_dotenv  # Import the function to load environment variables
import os  # Import the OS module to interact with the operating system

# Load environment variables from the .env file
load_dotenv()

# Load the environment (defaults to "dev" if not specified).
ENV = os.getenv("ENV", "dev")

# Database configuration based on the environment.
if ENV == "production":
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),  # Database name
        "engine": "peewee.MySQLDatabase",  # Database engine
        "user": os.getenv("MYSQL_USER"),  # Database user
        "password": os.getenv("MYSQL_PASSWORD"),  # User password
        "host": os.getenv("MYSQL_HOST"),  # Database host
        "port": int(os.getenv("MYSQL_PORT")),  # Connection port
    }
else:
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),  # Database name
        "engine": "peewee.MySQLDatabase",  # Database engine
        "user": os.getenv("MYSQL_USER"),  # Database user
        "password": os.getenv("MYSQL_PASSWORD"),  # User password
        "host": os.getenv("MYSQL_HOST"),  # Database host
        "port": int(os.getenv("MYSQL_PORT")),  # Connection port
    }

