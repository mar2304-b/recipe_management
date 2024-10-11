from pydantic import BaseModel

class RecipeCategory(BaseModel):
    """
    Represents a recipe category.

    Attributes:
        id (Optional[int]): A unique identifier for the category. Defaults to None.
        name (str): The name of the category.
    """

    id: int = None
    name: str

    