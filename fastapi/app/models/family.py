from pydantic import BaseModel

class Family(BaseModel):
    """
    Represents a family model.

    Attributes:
        id (Optional[int]): A unique identifier for the family. Defaults to None.
        name (str): The name of the family.
    """

    id: int = None
    name: str

