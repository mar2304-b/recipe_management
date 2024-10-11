from datetime import datetime
from pydantic import BaseModel 

class ShoppingList(BaseModel):
    """
    Modelo de lista de compras.

    Atributos:
        id (int, opcional): Identificador único de la lista de compras. Por defecto, None.
        user_id (str): Identificador del usuario que creó la lista.
        created_at (datetime): Fecha y hora de creación de la lista.
    """
    id : int = None
    user_id : str
    created_at : datetime
    


