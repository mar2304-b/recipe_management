from pydantic import BaseModel

class UserModel(BaseModel):
    id: int = None
    username: str
    age: int
    weigth : float
    diabetic : bool = True
    email: str
    password: str
    account_type: int
    profile_picture: str = None
    role_id: int