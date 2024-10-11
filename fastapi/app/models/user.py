from pydantic import BaseModel

class User(BaseModel):
    """
    Represents a user for the application.

    Attributes:
        id (Optional[int]): A unique identifier for the user. Defaults to None.
        username (str): The username of the user.
        age (int): The age of the user.
        weight (float): The weight of the user.
        diabetic (Optional[bool]): Indicates if the user is diabetic. Defaults to True.
        email (str): The email address of the user.
        password (str): The password for the user account.
        account_type (int): The type of account for the user.
        profile_picture (Optional[str]): The URL of the profile picture. Defaults to None.
        role_id (int): The identifier for the user's role.
    """

    id: int = None
    username: str
    age: int
    weight: float  # Corrected spelling from 'weigth' to 'weight'
    diabetic: bool = True
    email: str
    password: str
    account_type: int
    profile_picture: str = None
    role_id: int
