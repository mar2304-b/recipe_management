from datetime import date, datetime
from pydantic import BaseModel

class MenuModel(BaseModel):
    id: int = None
    user_id : int
    menu_date : date
    meal_type : str
    create_at : datetime = None

    
