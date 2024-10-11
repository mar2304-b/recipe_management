from pydantic import BaseModel

class Recipe(BaseModel):
    """
    Modelo de receta.

    Atributos:
        id (int, opcional): Identificador único de la receta. Por defecto, None.
        user_id (int, opcional): Identificador del usuario que creó la receta. Por defecto, None.
        description (str): Descripción de la receta.
        instructions (str): Instrucciones para preparar la receta.
        preparation_time (int): Tiempo de preparación en minutos.
        difficulty (str): Nivel de dificultad de la receta.
        is_public (bool, opcional): Indica si la receta es pública. Por defecto, True.
        nutrional_table (str): Información nutricional de la receta.
    """
    id : int = None
    user_id : int = None
    description : str
    instructions : str
    preparation_time : int
    difficulty : str
    is_public : bool = True
    nutrional_table : str