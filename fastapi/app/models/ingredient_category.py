from pydantic import BaseModel

class IngredientCategoryModel(BaseModel):
    id : int = None
    name : str
    