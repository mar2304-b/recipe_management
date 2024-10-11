from pydantic import BaseModel

class UserRole(BaseModel):
    """
    Represents a user role.

    Attributes:
        id (Optional[int]): A unique identifier for the role. Defaults to None.
        name (str): The name of the role.
        permissions (str): Permissions associated with the role.
    """

    id: int = None
    name: str
    permissions: str
