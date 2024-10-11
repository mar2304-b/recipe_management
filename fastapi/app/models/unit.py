from pydantic import BaseModel

class Unit(BaseModel):
    """
    Represents a unit of measurement.

    Attributes:
        id (Optional[int]): A unique identifier for the unit. Defaults to None.
        name (str): The name of the unit.
    """

    id: int = None
    name: str
