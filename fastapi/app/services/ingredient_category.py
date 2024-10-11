from config.database import IngredientCategoryModel
from models.ingredient_category import IngredientCategory

def get_all_ingredient_categories():
    """
    Retrieve all ingredient categories from the database.

    Returns:
        list: A list of ingredient categories as dictionaries.
    """
    ingredient_categories = IngredientCategoryModel.select().dicts()
    return list(ingredient_categories)

def get_ingredient_category_by_id(ingredient_category_id: int):
    """
    Retrieve a specific ingredient category by its ID.

    Args:
        ingredient_category_id (int): The ID of the ingredient category to retrieve.

    Returns:
        IngredientCategory or dict: The ingredient category if found, or an error dictionary.
    """
    try:
        ingredient_category = IngredientCategoryModel.get(IngredientCategoryModel.id == ingredient_category_id)
        return ingredient_category
    except IngredientCategoryModel.DoesNotExist:
        return {"error": "Ingredient category not found"}

def create_ingredient_category(ingredient_category: IngredientCategory):
    """
    Create a new ingredient category in the database.

    Args:
        ingredient_category (IngredientCategory): Ingredient category object containing details to create.

    Returns:
        IngredientCategory: The created ingredient category object.
    """
    category_instance = IngredientCategoryModel.create(
        name=ingredient_category.name,
    )
    return category_instance

def update_ingredient_category(ingredient_category_id: int, ingredient_category: IngredientCategory):
    """
    Update an existing ingredient category.

    Args:
        ingredient_category_id (int): The ID of the ingredient category to update.
        ingredient_category (IngredientCategory): Ingredient category object containing updated details.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        IngredientCategoryModel.update(
            {
                IngredientCategoryModel.name: ingredient_category.name,
            }
        )
        .where(IngredientCategoryModel.id == ingredient_category_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Ingredient category not found"}
    return {"message": "Ingredient category updated successfully"}

def delete_ingredient_category(ingredient_category_id: int):
    """
    Delete an ingredient category from the database.

    Args:
        ingredient_category_id (int): The ID of the ingredient category to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        ingredient_category = IngredientCategoryModel.get(IngredientCategoryModel.id == ingredient_category_id)
        ingredient_category.delete_instance()
    except IngredientCategoryModel.DoesNotExist:
        return {"error": "Ingredient category not found"}
    return {"message": "Ingredient category deleted successfully"}
