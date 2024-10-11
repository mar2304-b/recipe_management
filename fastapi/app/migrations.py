from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Boolean, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

# Base declarative for model classes
Base = declarative_base()

class UserRole(Base):
    """
    Database model representing a user role.

    Attributes:
        id (int): Unique identifier for the role.
        name (str): Name of the role, must be unique and not null.
        permissions (str): Permissions associated with the role, cannot be null.
    """
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    permissions = Column(String(255), nullable=False)

class UserFamily(Base):
    """
    Database model representing user families.

    Attributes:
        id (int): Unique identifier for the family.
        name (str): Name of the family, must be unique and not null.
    """
    __tablename__ = "user_families"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class User(Base):
    """
    Database model representing a user.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Unique username, must not be null.
        age (int): Age of the user, cannot be null.
        weight (float): Weight of the user, cannot be null.
        diabetic (bool): Indicates if the user is diabetic, defaults to False.
        email (str): Unique email address, cannot be null.
        password (str): User's password, cannot be null.
        account_type (int): Type of the user's account, cannot be null.
        profile_picture (str): URL of the user's profile picture, can be null.
        role_id (int): Foreign key referencing the user's role, cannot be null.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)  # Fixed typo from 'weigth' to 'weight'
    diabetic = Column(Boolean, default=False, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    account_type = Column(Integer, nullable=False)
    profile_picture = Column(String(100), nullable=True)
    role_id = Column(Integer, ForeignKey('user_roles.id'), nullable=False)

class Family(Base):
    """Database model representing a family."""
    __tablename__ = "families"  # Changed from 'family' to 'families' for consistency
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

class IngredientCategory(Base):
    """Database model representing ingredient categories."""
    __tablename__ = "ingredients_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), unique=True, nullable=False)

class Ingredient(Base):
    """
    Database model representing an ingredient.

    Attributes:
        id (int): Unique identifier for the ingredient.
        name (str): Unique name of the ingredient, cannot be null.
        unit_id (int): Foreign key referencing the ingredient's unit, cannot be null.
        expiration_date (Date): Expiration date of the ingredient, cannot be null.
        category_id (int): Foreign key referencing the ingredient's category, cannot be null.
        calories (int): Caloric content of the ingredient, cannot be null.
    """
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), unique=True, nullable=False)
    unit_id = Column(Integer, ForeignKey('units.id'), nullable=False)  # Fixed ForeignKey to match table name
    expiration_date = Column(Date, nullable=False)  # Fixed incorrect usage of 'date()'
    category_id = Column(Integer, ForeignKey('ingredients_categories.id'), nullable=False)
    calories = Column(Integer, nullable=False)

class Menu(Base):
    """
    Database model representing a menu.

    Attributes:
        id (int): Unique identifier for the menu.
        user_id (int): Foreign key referencing the user associated with the menu, cannot be null.
        menu_date (Date): Date of the menu, cannot be null.
        meal_type (str): Type of meal, must be unique and cannot be null.
        created_at (DateTime): Timestamp of when the menu was created.
    """
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    menu_date = Column(Date, nullable=False)  # Fixed incorrect usage of 'date()'
    meal_type = Column(String(80), nullable=False)
    created_at = Column(DateTime, nullable=False)

class Recipe(Base):
    """
    Database model representing a recipe.

    Attributes:
        id (int): Unique identifier for the recipe.
        user_id (int): Foreign key referencing the user who created the recipe, cannot be null.
        description (str): Description of the recipe, must be unique and cannot be null.
        instructions (str): Instructions for preparing the recipe, must be unique and cannot be null.
        preparation_time (int): Time taken to prepare the recipe, cannot be null.
        difficulty (str): Difficulty level of the recipe, must be unique and cannot be null.
        is_public (bool): Indicates if the recipe is public, cannot be null.
        nutritional_table (str): Nutritional information of the recipe, must be unique and cannot be null.
    """
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String(80), unique=True, nullable=False)
    instructions = Column(String(80), unique=True, nullable=False)
    preparation_time = Column(Integer, nullable=False)
    difficulty = Column(String(80), nullable=False)  # Removed 'unique' to allow multiple recipes of the same difficulty
    is_public = Column(Boolean, nullable=False)
    nutritional_table = Column(String(80), nullable=False)  # Removed 'unique'

class RecipeCategory(Base):
    """Database model representing recipe categories."""
    __tablename__ = "recipe_categories"  # Changed from 'recipe_category' for consistency
    id = Column(Integer, primary_key=True, index=True)

class ShoppingList(Base):
    """Database model representing a shopping list."""
    __tablename__ = "shopping_lists"  # Changed from 'shopping_list' for consistency
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)

class Unit(Base):
    """Database model representing measurement units."""
    __tablename__ = "units"  # Changed from 'unit' for consistency
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), unique=True, nullable=False)

# Database configuration
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)

# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
