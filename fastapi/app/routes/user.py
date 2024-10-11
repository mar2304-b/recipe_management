from models.user import User
from services.user import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)
from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/")
def get_users():
    """
    Obtiene todos los usuarios.

    Returns:
        list: Lista de usuarios.
    """
    return get_all_users()

@user_router.get("/{id}")
def get_user(user_id: int):
    """
    Obtiene un usuario específico por su ID.

    Args:
        user_id (int): ID del usuario a obtener.

    Returns:
        UserModel or dict: El usuario si se encuentra, o un diccionario de error.
    """
    return get_user_by_id(user_id)

@user_router.post("/")
def register_user(user: User):
    """
    Registra un nuevo usuario.

    Args:
        user (UserModel): Objeto de usuario con los detalles a crear.

    Returns:
        UserModel: El usuario creado.
    """
    return create_user(user)

@user_router.put("/{id}")
def update_user_data(user_id: int, user: User):
    """
    Actualiza los datos de un usuario existente.

    Args:
        user_id (int): ID del usuario a actualizar.
        user (UserModel): Objeto de usuario con los nuevos detalles.

    Returns:
        dict: Mensaje de éxito o error.
    """
    return update_user(user_id, user)

@user_router.delete("/{id}")
def remove_user(user_id: int):
    """
    Elimina un usuario de la base de datos.

    Args:
        user_id (int): ID del usuario a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    return delete_user(user_id)
