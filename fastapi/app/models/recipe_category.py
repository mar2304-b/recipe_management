from pydantic import BaseModel

class RecipeCategoryModel(BaseModel):
    id : int = None
    name : str
    