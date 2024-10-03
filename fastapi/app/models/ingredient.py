from datetime import date
from pydantic import BaseModel

class IngredientModel(BaseModel):
    id: int = None
    name: str
    unit_id : int
    expiration_date = date
    category_id : int
    calories: int
    