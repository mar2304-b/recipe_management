from pydantic import BaseModel

class RecipeCategoryModel(BaseModel):
    """
    Modelo de categoría de receta.

    Atributos:
        id (int, opcional): Identificador único de la categoría. Por defecto, None.
        name (str): Nombre de la categoría.
    """
    id : int = None
    name : str
    