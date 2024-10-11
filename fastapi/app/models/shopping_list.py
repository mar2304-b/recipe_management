from datetime import datetime
from pydantic import BaseModel

class ShoppingList(BaseModel):
    """
    Represents a shopping list.

    Attributes:
        id (Optional[int]): A unique identifier for the shopping list. Defaults to None.
        user_id (str): The identifier of the user who created the list.
        created_at (datetime): The date and time when the list was created.
    """

    id: int = None
    user_id: str
    created_at: datetime

    


