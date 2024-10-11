from datetime import date, datetime
from pydantic import BaseModel

class Menu(BaseModel):
    """
    Represents a menu.

    Attributes:
        id (Optional[int]): A unique identifier for the menu. Defaults to None.
        user_id (int): The identifier of the user who created the menu.
        menu_date (date): The date of the menu.
        meal_type (str): The type of meal (e.g., breakfast, lunch, dinner).
        create_at (Optional[datetime]): The date and time when the menu was created. Defaults to None.
    """

    id: int = None
    user_id: int
    menu_date: date
    meal_type: str
    create_at: datetime = None
