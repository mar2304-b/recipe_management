from pydantic import BaseModel

class Unit(BaseModel):
    """
    Modelo de unidad.

    Atributos:
        id (int, opcional): Identificador único de la unidad. Por defecto, None.
        name (str): Nombre de la unidad.
    """
    id: int = None
    name: str