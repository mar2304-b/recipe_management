from config.database import RecipeModel
from models.recipe import Recipe

def get_all_recipes():
    """Retrieve all recipes from the database.

    Returns:
        list: A list of recipes as dictionaries.
    """
    recipes = RecipeModel.select().dicts()
    return list(recipes)

def get_recipe_by_id(recipe_id: int):
    """Retrieve a specific recipe by its ID.

    Args:
        recipe_id (int): The ID of the recipe to retrieve.

    Returns:
        Recipe or dict: The recipe if found, or an error dictionary.
    """
    try:
        recipe = RecipeModel.get(RecipeModel.id == recipe_id)
        return recipe
    except RecipeModel.DoesNotExist:
        return {"error": "Recipe not found"}

def create_recipe(recipe: Recipe):
    """Create a new recipe in the database.

    Args:
        recipe (Recipe): The recipe object with details to create.

    Returns:
        Recipe: The created recipe object.
    """
    RecipeModel.create(
        user_id=recipe.user_id,
        description=recipe.description,
        instructions=recipe.instructions,
        preparation_time=recipe.preparation_time,
        difficulty=recipe.difficulty,
        is_public=recipe.is_public,
        nutrional_table=recipe.nutrional_table
    )
    
    return recipe

def update_recipe(recipe_id: int, recipe: Recipe):
    """Update an existing recipe.

    Args:
        recipe_id (int): The ID of the recipe to update.
        recipe (Recipe): The recipe object with updated details.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        RecipeModel.update(
            {
                RecipeModel.user_id: recipe.user_id,
                RecipeModel.description: recipe.description,
                RecipeModel.instructions: recipe.instructions,
                RecipeModel.preparation_time: recipe.preparation_time,
                RecipeModel.difficulty: recipe.difficulty,
                RecipeModel.is_public: recipe.is_public,
                RecipeModel.nutrional_table: recipe.nutrional_table,
            }
        )
        .where(RecipeModel.id == recipe_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Recipe not found"}
    return {"message": "Recipe updated successfully"}

def delete_recipe(recipe_id: int):
    """Delete a recipe from the database.

    Args:
        recipe_id (int): The ID of the recipe to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        recipe = RecipeModel.get(RecipeModel.id == recipe_id)
        recipe.delete_instance()
    except RecipeModel.DoesNotExist:
        return {"error": "Recipe not found"}
    return {"message": "Recipe deleted successfully"}

