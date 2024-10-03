from pydantic import BaseModel

class UnitModel(BaseModel):
    id: int = None
    name: str