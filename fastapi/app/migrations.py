from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

Base = declarative_base()

class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    role = Column(String(100), unique=True, nullable=False)
    
class userFamilies(Base):
    __tablename__ = "user_families"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class User(Base):
    __tablename__ ="users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False)
    age = Column(Integer, unique=)
    


# config database
DATABASE_URL = f"mysql+pymysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}/{DATABASE["name"]}"
engine = create_engine(DATABASE_URL)

# create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)