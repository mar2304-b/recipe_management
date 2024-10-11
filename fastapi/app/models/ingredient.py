from datetime import date
from pydantic import BaseModel

class Ingredient(BaseModel):
    """
    Represents an ingredient.

    Attributes:
        id (Optional[int]): A unique identifier for the ingredient. Defaults to None.
        name (str): The name of the ingredient.
        unit_id (int): The identifier for the unit of measurement.
        expiration_date (date): The expiration date of the ingredient.
        category_id (int): The identifier for the ingredient's category.
        calories (int): The number of calories per serving of the ingredient.
    """

    id: int = None
    name: str
    unit_id: int
    expiration_date: date
    category_id: int
    calories: int
