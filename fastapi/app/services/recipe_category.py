from config.database import RecipeCategoryModel
from models.recipe_category import RecipeCategory

def get_all_recipe_categories():
    """Retrieve all recipe categories from the database.

    Returns:
        list: A list of recipe categories as dictionaries.
    """
    recipe_categories = RecipeCategoryModel.select().dicts()
    return list(recipe_categories)

def get_recipe_category_by_id(recipe_category_id: int):
    """Retrieve a specific recipe category by its ID.

    Args:
        recipe_category_id (int): The ID of the recipe category to retrieve.

    Returns:
        RecipeCategory or dict: The recipe category if found, or an error dictionary.
    """
    try:
        recipe_category = RecipeCategoryModel.get(RecipeCategoryModel.id == recipe_category_id)
        return recipe_category
    except RecipeCategoryModel.DoesNotExist:
        return {"error": "Recipe category not found"}

def create_recipe_category(recipe_category: RecipeCategory):
    """Create a new recipe category in the database.

    Args:
        recipe_category (RecipeCategory): The recipe category object to create.

    Returns:
        RecipeCategory: The created recipe category object.
    """
    RecipeCategoryModel.create(
        name=recipe_category.name,
    )
    return recipe_category

def update_recipe_category(recipe_category_id: int, recipe_category: RecipeCategory):
    """Update an existing recipe category.

    Args:
        recipe_category_id (int): The ID of the recipe category to update.
        recipe_category (RecipeCategory): The recipe category object with updated details.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        RecipeCategoryModel.update(
            {
                RecipeCategoryModel.name: recipe_category.name,
            }
        )
        .where(RecipeCategoryModel.id == recipe_category_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Recipe category not found"}
    return {"message": "Recipe category updated successfully"}

def delete_recipe_category(recipe_category_id: int):
    """Delete a recipe category from the database.

    Args:
        recipe_category_id (int): The ID of the recipe category to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        recipe_category = RecipeCategoryModel.get(RecipeCategoryModel.id == recipe_category_id)
        recipe_category.delete_instance()
    except RecipeCategoryModel.DoesNotExist:
        return {"error": "Recipe category not found"}
    return {"message": "Recipe category deleted successfully"}

