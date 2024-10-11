from models.user_role import UserRole
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
    Retrieve all user roles.

    Returns:
        list: A list of all user roles.
    """
    return get_all_user_roles()

@user_role_router.get("/{user_role_id}")
def get_user_role(user_role_id: int):
    """
    Retrieve a specific user role by its ID.

    Args:
        user_role_id (int): The ID of the user role to retrieve.

    Returns:
        UserRole or dict: The user role if found, or an error dictionary.
    """
    return get_user_role_by_id(user_role_id)

@user_role_router.post("/")
def register_user_role(user_role: UserRole):
    """
    Register a new user role.

    Args:
        user_role (UserRole): UserRole object containing details for the new role.

    Returns:
        UserRole: The created user role object.
    """
    return create_user_role(user_role)

@user_role_router.put("/{user_role_id}")
def update_user_role_data(user_role_id: int, user_role: UserRole):
    """
    Update the data of an existing user role.

    Args:
        user_role_id (int): The ID of the user role to update.
        user_role (UserRole): UserRole object containing updated details.

    Returns:
        dict: A message indicating success or error.
    """
    return update_user_role(user_role_id, user_role)

@user_role_router.delete("/{user_role_id}")
def remove_user_role(user_role_id: int):
    """
    Delete a user role from the database.

    Args:
        user_role_id (int): The ID of the user role to delete.

    Returns:
        dict: A message indicating success or error.
    """
    return delete_user_role(user_role_id)
