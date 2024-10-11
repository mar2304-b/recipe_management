from config.database import UserModel  # Import the user model
from models.user import User  # Import the User class

def get_all_users():
    """Retrieve all users from the database.

    Returns:
        list: A list of users as dictionaries.
    """
    users = UserModel.select().dicts()  # Select all users as dictionaries
    return list(users)  # Return the list of users

def get_user_by_id(user_id: int):
    """Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to find.

    Returns:
        UserModel or dict: The found user or an error message if not found.
    """
    try:
        user = UserModel.get(UserModel.id == user_id)  # Find the user by ID
        return user  # Return the found user
    except UserModel.DoesNotExist:  # Handle case where the user does not exist
        return {"error": "User not found"}  # Return an error message

def create_user(user: User):
    """Create a new user in the database.

    Args:
        user (User): The user object with the new user information.

    Returns:
        User: The created user.
    """
    UserModel.create(
        username=user.username,
        age=user.age,
        weight=user.weight,  # Fixed typo: "weigth" to "weight"
        diabetic=user.diabetic,
        email=user.email,
        password=user.password,
        account_type=user.account_type,
        profile_picture=user.profile_picture,
        role_id=user.role_id,
    )
    return user  # Return the created user

def update_user(user_id: int, user: User):
    """Update an existing user.

    Args:
        user_id (int): The ID of the user to update.
        user (User): The user object with updated information.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        UserModel.update(
            {
                UserModel.username: user.username,
                UserModel.age: user.age,
                UserModel.weight: user.weight,  # Fixed typo here as well
                UserModel.diabetic: user.diabetic,
                UserModel.email: user.email,
                UserModel.password: user.password,
                UserModel.account_type: user.account_type,
                UserModel.profile_picture: user.profile_picture,
                UserModel.role_id: user.role_id,
            }
        )
        .where(UserModel.id == user_id)  # Filter by ID
        .execute()  # Execute the update
    )

    if updated_rows == 0:  # Check if any rows were updated
        return {"error": "User not found"}  # Return an error message
    return {"message": "User updated successfully"}  # Return a success message

def delete_user(user_id: int):
    """Delete a user by their ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        user = UserModel.get(UserModel.id == user_id)  # Find the user by ID
        user.delete_instance()  # Delete the found user
    except UserModel.DoesNotExist:  # Handle case where the user does not exist
        return {"error": "User not found"}  # Return an error message
    return {"message": "User deleted successfully"}  # Return a success message
