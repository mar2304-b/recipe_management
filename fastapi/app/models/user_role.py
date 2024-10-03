from pydantic import BaseModel  

class UserRoleModel(BaseModel):
    id: int = None
    name: str
    permissions : str
    