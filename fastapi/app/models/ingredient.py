from datetime import date
from pydantic import BaseModel

class Ingredient(BaseModel):
    """
    Modelo de ingrediente.

    Atributos:
        id (int, opcional): Identificador único del ingrediente. Por defecto, None.
        name (str): Nombre del ingrediente.
        unit_id (int): Identificador de la unidad de medida.
        expiration_date (date): Fecha de vencimiento del ingrediente.
        category_id (int): Identificador de la categoría del ingrediente.
        calories (int): Cantidad de calorías por porción del ingrediente.
    """
    id: int = None
    name: str
    unit_id : int
    expiration_date : date
    category_id : int
    calories: int