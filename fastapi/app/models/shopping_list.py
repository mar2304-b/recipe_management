from datetime import datetime
from pydantic import BaseModel 

class ShoppingListModel(BaseModel):
    id : int = None
    user_id = str
    created_at : datetime
    


