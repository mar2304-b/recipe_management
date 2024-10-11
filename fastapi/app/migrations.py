from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

# Base declarative para las clases del modelo
Base = declarative_base()

class UserRole(Base):
    """
    Modelo de base de datos que representa el rol de usuario.

    Attributes:
        id (int): Identificador único del rol.
        name (str): Nombre del rol, debe ser único y no nulo.
        role (str): Descripción del rol, debe ser único y no nulo.
    """
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    permissions = Column(String(255), nullable=False)

class userFamilies(Base):
    """
    Modelo de base de datos que representa las familias de los usuarios.

    Attributes:
        id (int): Identificador único de la familia.
        name (str): Nombre de la familia, debe ser único y no nulo.
    """
    __tablename__ = "user_families"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class User(Base):
    """
    Modelo de base de datos que representa a un usuario.

    Attributes:
        id (int): Identificador único del usuario.
        username (str): Nombre de usuario, debe ser único y no nulo.
        age (int): Edad del usuario, no nulo.
        weigth (float): Peso del usuario, no nulo.
        diabetic (bool): Indica si el usuario es diabético, por defecto es False.
        email (str): Correo electrónico del usuario, debe ser único y no nulo.
        password (str): Contraseña del usuario, no nulo.
        account_type (int): Tipo de cuenta del usuario, no nulo.
        profile_picture (str): URL de la imagen de perfil del usuario, puede ser nulo.
        role_id (int): ID del rol asociado al usuario, debe ser no nulo.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    weigth = Column(Float, nullable=False)
    diabetic = Column(Boolean, default=False, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    account_type = Column(Integer, nullable=False)
    profile_picture = Column(String(100), nullable=True)
    role_id = Column(Integer, ForeignKey('user_roles.id'), nullable=False)
    
class IngredientCategory(Base):
    __tablename__ = "ingredients_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), unique=True, nullable=False)

# Configuración de la base de datos
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)

# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
