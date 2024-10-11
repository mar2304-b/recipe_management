from pydantic import BaseModel

class Family(BaseModel):
    """
    Modelo de familia.

    Atributos:
        id (int, opcional): Identificador único de la familia. Por defecto, None.
        name (str): Nombre de la familia.
    """
    id: int = None
    name : str
