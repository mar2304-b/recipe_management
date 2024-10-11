from pydantic import BaseModel  

class UserRole(BaseModel):
    """
    Modelo de roles de usuario.

    Atributos:
        id (int, opcional): Identificador único del rol. Por defecto, None.
        name (str): Nombre del rol.
        permissions (str): Permisos asociados al rol.
    """
    id: int = None
    name: str
    permissions : str