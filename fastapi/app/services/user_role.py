from config.database import UserRoleModel  # Import the user role model
from models.user_role import UserRole  # Import the UserRole class

def get_all_user_roles():
    """Retrieve all user roles from the database.

    Returns:
        list: A list of user roles as dictionaries.
    """
    user_roles = UserRoleModel.select().dicts()  # Select all user roles as dictionaries
    return list(user_roles)  # Return the list of user roles

def get_user_role_by_id(user_role_id: int):
    """Retrieve a user role by its ID.

    Args:
        user_role_id (int): The ID of the user role to find.

    Returns:
        UserRoleModel or dict: The found user role or an error message if not found.
    """
    try:
        user_role = UserRoleModel.get(UserRoleModel.id == user_role_id)  # Find the role by ID
        return user_role  # Return the found role
    except UserRoleModel.DoesNotExist:  # Handle case where the role does not exist
        return {"error": "User role not found"}  # Return an error message

def create_user_role(user_role: UserRole):
    """Create a new user role in the database.

    Args:
        user_role (UserRole): The user role object with new role information.

    Returns:
        UserRole: The created user role.
    """
    UserRoleModel.create(
        name=user_role.name,
        permissions=user_role.permissions,
    )
    return user_role  # Return the created user role

def update_user_role(user_role_id: int, user_role: UserRole):
    """Update an existing user role.

    Args:
        user_role_id (int): The ID of the user role to update.
        user_role (UserRole): The user role object with updated information.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        UserRoleModel.update(
            {
                UserRoleModel.name: user_role.name,
                UserRoleModel.permissions: user_role.permissions,
            }
        )
        .where(UserRoleModel.id == user_role_id)  # Filter by ID
        .execute()  # Execute the update
    )

    if updated_rows == 0:  # Check if any rows were updated
        return {"error": "User role not found"}  # Return an error message
    return {"message": "User role updated successfully"}  # Return a success message

def delete_user_role(user_role_id: int):
    """Delete a user role by its ID.

    Args:
        user_role_id (int): The ID of the user role to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        user_role = UserRoleModel.get(UserRoleModel.id == user_role_id)  # Find the role by ID
        user_role.delete_instance()  # Delete the found role
    except UserRoleModel.DoesNotExist:  # Handle case where the role does not exist
        return {"error": "User role not found"}  # Return an error message
    return {"message": "User role deleted successfully"}  # Return a success message

