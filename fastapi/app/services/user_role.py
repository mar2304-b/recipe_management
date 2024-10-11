from config.database import UserRoleModel  # Importa el modelo de rol de usuario
from models.user_role  import UserRole  # Importa la clase UserRole

def get_all_user_roles():
    """Obtiene todos los roles de usuario de la base de datos."""
    user_roles = UserRole.select().dicts()  # Selecciona todos los roles como diccionarios
    return list(user_roles)  # Retorna la lista de roles de usuario

def get_user_role_by_id(user_role_id: int):
    """Obtiene un rol de usuario por su ID.

    Args:
        user_role_id (int): El ID del rol de usuario a buscar.

    Returns:
        UserRoleModel: El rol de usuario encontrado o un mensaje de error si no existe.
    """
    try:
        user_role = UserRole.get(UserRole.id == user_role_id)  # Busca el rol por ID
        return user_role  # Retorna el rol encontrado
    except UserRole.DoesNotExist:  # Captura si el rol no existe
        return {"error": "User role not found"}  # Retorna un mensaje de error

def create_user_role(user_role: UserRole):
    """Crea un nuevo rol de usuario en la base de datos.

    Args:
        user_role (UserRole): El objeto rol de usuario con la información del nuevo rol.

    Returns:
        UserRole: El rol de usuario creado.
    """
    UserRoleModel.create(
        name=user_role.name,
        permissions=user_role.permissions,
    )
    return user_role  # Retorna el rol de usuario creado

def update_user_role(user_role_id: int, user_role: UserRole):
    """Actualiza un rol de usuario existente.

    Args:
        user_role_id (int): El ID del rol de usuario a actualizar.
        user_role (UserRole): El objeto rol de usuario con la nueva información.

    Returns:
        dict: Mensaje de éxito o error.
    """
    updated_rows = (
        UserRoleModel.update(
            {
                UserRole.name: user_role.name,
                UserRole.permissions: user_role.permissions,
            }
        )
        .where(UserRole.id == user_role_id)  # Filtra por ID
        .execute()  # Ejecuta la actualización
    )

    if updated_rows == 0:  # Verifica si se actualizó algún registro
        return {"error": "User role not found"}  # Retorna un mensaje de error
    return {"message": "User role updated successfully"}  # Retorna un mensaje de éxito

def delete_user_role(user_role_id: int):
    """Elimina un rol de usuario por su ID.

    Args:
        user_role_id (int): El ID del rol de usuario a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        user_role = UserRoleModel.get(UserRole.id == user_role_id)  # Busca el rol por ID
        user_role.delete_instance()  # Elimina el rol encontrado
    except UserRole.DoesNotExist:  # Captura si el rol no existe
        return {"error": "User role not found"}  # Retorna un mensaje de error
    return {"message": "User role deleted successfully"}  # Retorna un mensaje de éxito
