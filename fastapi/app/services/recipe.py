from config.database import RecipeModel
from models.recipe import Recipe

def get_all_recipes():
    """ 
    Obtiene todas las recetas de la base de datos.

    Returns:
        list: Lista de recetas como diccionarios.
    """
    recipes = RecipeModel.select().dicts()
    return list(recipes)

def get_recipe_by_id(recipe_id: int):
    """
    Obtiene una receta específica por su ID.

    Args:
        recipe_id (int): ID de la receta a obtener.

    Returns:
        Recipe or dict: La receta si se encuentra, o un diccionario de error.
    """
    try:
        recipe = RecipeModel.get(RecipeModel.id == recipe_id)
        return recipe
    except RecipeModel.DoesNotExist:
        return {"error": "Recipe not found"}

def create_recipe(recipe: Recipe):
    """
    Crea una nueva receta en la base de datos.

    Args:
        recipe (Recipe): Objeto de receta con los detalles a crear.

    Returns:
        Recipe: La receta creada.
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
    """
    Actualiza una receta existente.

    Args:
        recipe_id (int): ID de la receta a actualizar.
        recipe (Recipe): Objeto de receta con los nuevos detalles.

    Returns:
        dict: Mensaje de éxito o error.
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
    """
    Elimina una receta de la base de datos.

    Args:
        recipe_id (int): ID de la receta a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        recipe = RecipeModel.get(RecipeModel.id == recipe_id)
        recipe.delete_instance()
    except RecipeModel.DoesNotExist:
        return {"error": "Recipe not found"}
    return {"message": "Recipe deleted successfully"}
