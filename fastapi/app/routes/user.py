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
    Retrieve all users.

    Returns:
        list: A list of all users.
    """
    return get_all_users()

@user_router.get("/{user_id}")
def get_user(user_id: int):
    """
    Retrieve a specific user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User or dict: The user if found, or an error dictionary.
    """
    return get_user_by_id(user_id)

@user_router.post("/")
def register_user(user: User):
    """
    Register a new user.

    Args:
        user (User): User object containing details for the new user.

    Returns:
        User: The created user object.
    """
    return create_user(user)

@user_router.put("/{user_id}")
def update_user_data(user_id: int, user: User):
    """
    Update the data of an existing user.

    Args:
        user_id (int): The ID of the user to update.
        user (User): User object containing updated details.

    Returns:
        dict: A message indicating success or error.
    """
    return update_user(user_id, user)

@user_router.delete("/{user_id}")
def remove_user(user_id: int):
    """
    Delete a user from the database.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        dict: A message indicating success or error.
    """
    return delete_user(user_id)

