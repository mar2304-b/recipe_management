from pydantic import BaseModel

class User(BaseModel):
    """
    Modelo de usuario para la aplicación.

    Atributos:
        id (int, opcional): Identificador único del usuario. Por defecto, None.
        username (str): Nombre de usuario.
        age (int): Edad del usuario.
        weigth (float): Peso del usuario.
        diabetic (bool, opcional): Indica si el usuario es diabético. Por defecto, True.
        email (str): Correo electrónico del usuario.
        password (str): Contraseña del usuario.
        account_type (int): Tipo de cuenta del usuario.
        profile_picture (str, opcional): URL de la imagen de perfil. Por defecto, None.
        role_id (int): Identificador del rol del usuario.
    """
    id: int = None
    username: str
    age: int
    weigth : float
    diabetic : bool = True
    email: str
    password: str
    account_type: int
    profile_picture: str = None
    role_id: int