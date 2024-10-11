from pydantic import BaseModel

class IngredientCategory(BaseModel):
    """
    Modelo de categoría de ingredientes.

    Atributos:
        id (int, opcional): Identificador único de la categoría. Por defecto, None.
        name (str): Nombre de la categoría.
    """
    id : int = None
    name : str
    