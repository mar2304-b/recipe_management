from config.database import IngredientCategoryModel

from models.ingredient_category import IngredientCategory

def get_all_ingredient_categories():
    ingredient_categories = IngredientCategoryModel.select().dicts()
    return list(ingredient_categories)

def get_ingredient_category_by_id(ingredient_category_id: int):
    
    try:
        ingredient_category = IngredientCategoryModel.get(IngredientCategoryModel.id == ingredient_category_id)
        return ingredient_category
    except IngredientCategoryModel.DoesNotExist:
        return {"error": "Ingredient category not found"}
    
def create_ingredient_category(ingredient_category : IngredientCategory):

    IngredientCategoryModel.create(
         
        name = ingredient_category.name,
     
  
    )
    return ingredient_category

def update_ingredient_category(ingredient_category_id: int, ingredient_category: IngredientCategory):
    
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
    
    try:
        ingredient_category = IngredientCategoryModel.get(IngredientCategoryModel.id == ingredient_category_id)
        ingredient_category.delete_instance()
    except IngredientCategoryModel.DoesNotExist:
        return {"error": "Ingredient category not found"}
    return {"message": "Ingredient category deleted successfully"}