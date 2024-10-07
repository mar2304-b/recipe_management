from datetime import date, datetime
from pydantic import BaseModel

class MenuModel(BaseModel):
    """
    Modelo de menú.

    Atributos:
        id (int, opcional): Identificador único del menú. Por defecto, None.
        user_id (int): Identificador del usuario que creó el menú.
        menu_date (date): Fecha del menú.
        meal_type (str): Tipo de comida (desayuno, almuerzo, cena, etc.).
        create_at (datetime, opcional): Fecha y hora de creación del menú. Por defecto, None.
    """
    id: int = None
    user_id : int
    menu_date : date
    meal_type : str
    create_at : datetime = None
