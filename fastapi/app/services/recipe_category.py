from config.database import RecipeCategoryModel
from models.recipe_category import RecipeCategory

def get_all_recipe_categories():
    """
    Obtiene todas las categorías de recetas de la base de datos.

    Returns:
        list: Lista de categorías de recetas como diccionarios.
    """
    recipe_categories = RecipeCategoryModel.select().dicts()
    return list(recipe_categories)

def get_recipe_category_by_id(recipe_category_id: int):
    """
    Obtiene una categoría de receta específica por su ID.

    Args:
        recipe_category_id (int): ID de la categoría de receta a obtener.

    Returns:
        RecipeCategory or dict: La categoría de receta si se encuentra, o un diccionario de error.
    """
    try:
        recipe_category = RecipeCategoryModel.get(RecipeCategoryModel.id == recipe_category_id)
        return recipe_category
    except RecipeCategoryModel.DoesNotExist:
        return {"error": "Recipe category not found"}

def create_recipe_category(recipe_category: RecipeCategory):
    """
    Crea una nueva categoría de receta en la base de datos.

    Args:
        recipe_category (RecipeCategory): Objeto de categoría de receta con los detalles a crear.

    Returns:
        RecipeCategory: La categoría de receta creada.
    """
    RecipeCategoryModel.create(
        name=recipe_category.name,
    )
    return recipe_category

def update_recipe_category(recipe_category_id: int, recipe_category: RecipeCategory):
    """
    Actualiza una categoría de receta existente.

    Args:
        recipe_category_id (int): ID de la categoría de receta a actualizar.
        recipe_category (RecipeCategory): Objeto de categoría de receta con los nuevos detalles.

    Returns:
        dict: Mensaje de éxito o error.
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
    """
    Elimina una categoría de receta de la base de datos.

    Args:
        recipe_category_id (int): ID de la categoría de receta a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        recipe_category = RecipeCategoryModel.get(RecipeCategoryModel.id == recipe_category_id)
        recipe_category.delete_instance()
    except RecipeCategoryModel.DoesNotExist:
        return {"error": "Recipe category not found"}
    return {"message": "Recipe category deleted successfully"}
