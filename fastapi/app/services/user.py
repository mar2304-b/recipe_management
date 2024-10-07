from config.database import UserModel  # Importa el modelo de usuario
from models.user import User  # Importa la clase User

def get_all_users():
    """Obtiene todos los usuarios de la base de datos."""
    users = UserModel.select().dicts()  # Selecciona todos los usuarios como diccionarios
    return list(users)  # Retorna la lista de usuarios

def get_user_by_id(user_id: int):
    """Obtiene un usuario por su ID.

    Args:
        user_id (int): El ID del usuario a buscar.

    Returns:
        UserModel: El usuario encontrado o un mensaje de error si no existe.
    """
    try:
        user = UserModel.get(UserModel.id == user_id)  # Busca el usuario por ID
        return user  # Retorna el usuario encontrado
    except UserModel.DoesNotExist:  # Captura si el usuario no existe
        return {"error": "User not found"}  # Retorna un mensaje de error

def create_user(user: User):
    """Crea un nuevo usuario en la base de datos.

    Args:
        user (User): El objeto usuario con la información del nuevo usuario.

    Returns:
        User: El usuario creado.
    """
    UserModel.create(
        username=user.username,
        age=user.age,
        weigth=user.weigth,
        diabetic=user.diabetic,
        email=user.email,
        password=user.password,
        account_type=user.account_type,
        profile_picture=user.profile_picture,
        role_id=user.role_id,
    )
    return user  # Retorna el usuario creado

def update_user(user_id: int, user: User):
    """Actualiza un usuario existente.

    Args:
        user_id (int): El ID del usuario a actualizar.
        user (User): El objeto usuario con la nueva información.

    Returns:
        dict: Mensaje de éxito o error.
    """
    updated_rows = (
        UserModel.update(
            {
                UserModel.username: user.username,
                UserModel.age: user.age,
                UserModel.weigth: user.weigth,
                UserModel.diabetic: user.diabetic,
                UserModel.email: user.email,
                UserModel.password: user.password,
                UserModel.account_type: user.account_type,
                UserModel.profile_picture: user.profile_picture,
                UserModel.role_id: user.role_id,
            }
        )
        .where(UserModel.id == user_id)  # Filtra por ID
        .execute()  # Ejecuta la actualización
    )

    if updated_rows == 0:  # Verifica si se actualizó algún registro
        return {"error": "User not found"}  # Retorna un mensaje de error
    return {"message": "User updated successfully"}  # Retorna un mensaje de éxito

def delete_user(user_id: int):
    """Elimina un usuario por su ID.

    Args:
        user_id (int): El ID del usuario a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        user = UserModel.get(UserModel.id == user_id)  # Busca el usuario por ID
        user.delete_instance()  # Elimina el usuario encontrado
    except UserModel.DoesNotExist:  # Captura si el usuario no existe
        return {"error": "User not found"}  # Retorna un mensaje de error
    return {"message": "User deleted successfully"}  # Retorna un mensaje de éxito
