from peewee import *
from config.settings import DATABASE

# Imprime la configuración de la base de datos.
print(DATABASE)

# Configuración de la base de datos MySQL.
database = MySQLDatabase(
    DATABASE["name"],       # Nombre de la base de datos
    user=DATABASE["user"],  # Usuario de la base de datos
    password=DATABASE["password"],  # Contraseña del usuario
    host=DATABASE["host"],  # Host de la base de datos
    port=DATABASE["port"],  # Puerto de conexión
)

class UserModel(Model):
    """Modelo de usuario."""
    id = AutoField(primary_key=True)  # ID autogenerado
    username = CharField(max_length=50)  # Nombre de usuario
    age = IntegerField()  # Edad del usuario
    weigth = FloatField()  # Peso del usuario
    diabetic = BooleanField(default=False)  # Indica si el usuario es diabético
    email = CharField(max_length=50)  # Correo electrónico
    password = CharField(max_length=50)  # Contraseña
    account_type = CharField(max_length=50)  # Tipo de cuenta
    profile_picture = CharField()  # Ruta de la imagen de perfil
    role_id = IntegerField()  # ID del rol

    class Meta:
        database = database  # Asocia el modelo a la base de datos
        table_name = "users"  # Nombre de la tabla

class UserRoleModel(Model):
    """Modelo de rol de usuario."""
    id = AutoField(primary_key=True)  # ID autogenerado
    name = CharField(max_length=50)  # Nombre del rol
    permission = CharField(max_length=50)  # Permisos del rol

    class Meta:
        database = database
        table_name = "user_roles"

class UnitModel(Model):
    """Modelo de unidad de medida."""
    id = AutoField(primary_key=True)  # ID autogenerado
    name = CharField(max_length=50)  # Nombre de la unidad

    class Meta:
        database = database
        table_name = "units"

class ShoppingListModel(Model):
    """Modelo de lista de compras."""
    id = AutoField(primary_key=True)  # ID autogenerado
    user_id = CharField(max_length=50)  # ID del usuario
    created_at = DateTimeField()  # Fecha y hora de creación

    class Meta:
        database = database
        table_name = "shopping_lists"

class RecipeModel(Model):
    """Modelo de receta."""
    id = AutoField(primary_key=True)  # ID autogenerado
    user_id = IntegerField()  # ID del usuario
    description = CharField(max_length=100)  # Descripción de la receta
    instructions = CharField(max_length=100)  # Instrucciones
    preparation_time = IntegerField()  # Tiempo de preparación
    difficulty = CharField(max_length=100)  # Dificultad
    is_public = BooleanField(default=False)  # Indica si la receta es pública
    nutrional_table = CharField(max_length=100)  # Tabla nutricional

    class Meta:
        database = database
        table_name = "recipes"

class RecipeCategoryModel(Model):
    """Modelo de categoría de receta."""
    id = AutoField(primary_key=True)  # ID autogenerado
    name = CharField(max_length=50)  # Nombre de la categoría

    class Meta:
        database = database
        table_name = "recipe_categories"

class MenuModel(Model):
    """Modelo de menú."""
    id = AutoField(primary_key=True)  # ID autogenerado
    user_id = IntegerField()  # ID del usuario
    menu_date = DateField()  # Fecha del menú
    meal_type = CharField(max_length=50)  # Tipo de comida
    create_at = DateTimeField()  # Fecha y hora de creación

    class Meta:
        database = database
        table_name = "menus"

class IngredientModel(Model):
    """Modelo de ingrediente."""
    id = AutoField(primary_key=True)  # ID autogenerado
    name = CharField(max_length=50)  # Nombre del ingrediente
    unit_id = IntegerField()  # ID de la unidad de medida
    expiration_date = DateField()  # Fecha de vencimiento
    category_id = IntegerField()  # ID de la categoría
    calories = IntegerField()  # Calorías

    class Meta:
        database = database
        table_name = "ingredients"

class IngredientCategoryModel(Model):
    """Modelo de categoría de ingredientes."""
    id = AutoField(primary_key=True)  # ID autogenerado
    name = CharField(max_length=50)  # Nombre de la categoría

    class Meta:
        database = database
        table_name = "ingredient_category"

class FamilyModel(Model):
    """Modelo de familia."""
    id = AutoField(primary_key=True)  # ID autogenerado
    name = CharField(max_length=50)  # Nombre de la familia

    class Meta:
        database = database
        table_name = "families"
