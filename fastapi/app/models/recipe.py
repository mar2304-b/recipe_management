from pydantic import BaseModel

class RecipeModel(BaseModel):
    id : int = None
    user_id : int = None
    description : str
    instructions : str
    preparation_time : int
    difficulty : str
    is_public : bool = True
    nutrional_table : str
