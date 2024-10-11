from pydantic import BaseModel

class Recipe(BaseModel):
    """
    Represents a recipe.

    Attributes:
        id (Optional[int]): A unique identifier for the recipe. Defaults to None.
        user_id (Optional[int]): The identifier of the user who created the recipe. Defaults to None.
        description (str): A description of the recipe.
        instructions (str): Instructions for preparing the recipe.
        preparation_time (int): Preparation time in minutes.
        difficulty (str): The difficulty level of the recipe.
        is_public (Optional[bool]): Indicates if the recipe is public. Defaults to True.
        nutritional_table (str): Nutritional information of the recipe.
    """

    id: int = None
    user_id: int = None
    description: str
    instructions: str
    preparation_time: int
    difficulty: str
    is_public: bool = True
    nutritional_table: str
