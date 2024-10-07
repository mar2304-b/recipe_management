from models.user_role import UserRoleModel
from services.user_role import (
    get_all_user_roles,
    get_user_role_by_id,
    create_user_role,
    update_user_role,
    delete_user_role,
)
from fastapi import APIRouter

user_role_router = APIRouter()

@user_role_router.get("/")
def get_user_roles():
    """
    Obtiene todos los roles de usuario.

    Returns:
        list: Lista de roles de usuario.
    """
    return get_all_user_roles()

@user_role_router.get("/{id}")
def get_user_role(user_role_id: int):
    """
    Obtiene un rol de usuario específico por su ID.

    Args:
        user_role_id (int): ID del rol de usuario a obtener.

    Returns:
        UserRoleModel or dict: El rol de usuario si se encuentra, o un diccionario de error.
    """
    return get_user_role_by_id(user_role_id)

@user_role_router.post("/")
def register_user_role(user_role: UserRoleModel):
    """
    Registra un nuevo rol de usuario.

    Args:
        user_role (UserRoleModel): Objeto de rol de usuario con los detalles a crear.

    Returns:
        UserRoleModel: El rol de usuario creado.
    """
    return create_user_role(user_role)

@user_role_router.put("/{id}")
def update_user_role_data(user_role_id: int, user_role: UserRoleModel):
    """
    Actualiza los datos de un rol de usuario existente.

    Args:
        user_role_id (int): ID del rol de usuario a actualizar.
        user_role (UserRoleModel): Objeto de rol de usuario con los nuevos detalles.

    Returns:
        dict: Mensaje de éxito o error.
    """
    return update_user_role(user_role_id, user_role)

@user_role_router.delete("/{id}")
def remove_user_role(user_role_id: int):
    """
    Elimina un rol de usuario de la base de datos.

    Args:
        user_role_id (int): ID del rol de usuario a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    return delete_user_role(user_role_id)
