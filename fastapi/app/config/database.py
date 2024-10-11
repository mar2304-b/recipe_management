from peewee import *
from config.settings import DATABASE

# Print the database configuration for debugging purposes.
print(DATABASE)

# MySQL database configuration.
database = MySQLDatabase(
    DATABASE["name"],       # Database name
    user=DATABASE["user"],  # Database user
    password=DATABASE["password"],  # User password
    host=DATABASE["host"],  # Database host
    port=DATABASE["port"],  # Connection port
)

class UserModel(Model):
    """Represents a user in the system."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    username = CharField(max_length=50)  # Username
    age = IntegerField()  # User's age
    weight = FloatField()  # User's weight (corrected spelling)
    diabetic = BooleanField(default=False)  # Indicates if the user is diabetic
    email = CharField(max_length=50)  # User's email address
    password = CharField(max_length=50)  # User's password
    account_type = CharField(max_length=50)  # User's account type
    profile_picture = CharField(null=True)  # Profile picture URL (nullable)
    role_id = IntegerField()  # Role ID

    class Meta:
        database = database  # Associate model with the database
        table_name = "users"  # Database table name

class UserRoleModel(Model):
    """Represents a user role."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    name = CharField(max_length=50)  # Role name
    permissions = CharField(max_length=50)  # Role permissions

    class Meta:
        database = database
        table_name = "user_roles"

class UnitModel(Model):
    """Represents a unit of measurement."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    name = CharField(max_length=50)  # Unit name

    class Meta:
        database = database
        table_name = "units"

class ShoppingListModel(Model):
    """Represents a shopping list."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    user_id = CharField(max_length=50)  # User ID
    created_at = DateTimeField()  # Creation date and time

    class Meta:
        database = database
        table_name = "shopping_lists"

class RecipeModel(Model):
    """Represents a recipe."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    user_id = IntegerField()  # User ID
    description = CharField(max_length=100)  # Recipe description
    instructions = CharField(max_length=100)  # Preparation instructions
    preparation_time = IntegerField()  # Preparation time in minutes
    difficulty = CharField(max_length=100)  # Difficulty level
    is_public = BooleanField(default=False)  # Indicates if the recipe is public
    nutritional_table = CharField(max_length=100)  # Nutritional information

    class Meta:
        database = database
        table_name = "recipes"

class RecipeCategoryModel(Model):
    """Represents a recipe category."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    name = CharField(max_length=50)  # Category name

    class Meta:
        database = database
        table_name = "recipe_categories"

class MenuModel(Model):
    """Represents a menu."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    user_id = IntegerField()  # User ID
    menu_date = DateField()  # Menu date
    meal_type = CharField(max_length=50)  # Meal type
    created_at = DateTimeField()  # Creation date and time

    class Meta:
        database = database
        table_name = "menus"

class IngredientModel(Model):
    """Represents an ingredient."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    name = CharField(max_length=50)  # Ingredient name
    unit_id = IntegerField()  # Unit of measurement ID
    expiration_date = DateField()  # Expiration date
    category_id = IntegerField()  # Category ID
    calories = IntegerField()  # Calories

    class Meta:
        database = database
        table_name = "ingredients"

class IngredientCategoryModel(Model):
    """Represents an ingredient category."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    name = CharField(max_length=50)  # Category name

    class Meta:
        database = database
        table_name = "ingredient_category"

class FamilyModel(Model):
    """Represents a family."""
    id = AutoField(primary_key=True)  # Auto-generated ID
    name = CharField(max_length=50)  # Family name

    class Meta:
        database = database
        table_name = "families"
