from config.database import ShoppingListModel  # Import the shopping list model
from models.shopping_list import ShoppingList  # Import the ShoppingList class

def get_all_shopping_lists():
    """Retrieve all shopping lists from the database.

    Returns:
        list: A list of shopping lists as dictionaries.
    """
    shopping_lists = ShoppingListModel.select().dicts()  # Select all shopping lists as dictionaries
    return list(shopping_lists)  # Return the list of shopping lists

def get_shopping_list_by_id(shopping_list_id: int):
    """Retrieve a shopping list by its ID.

    Args:
        shopping_list_id (int): The ID of the shopping list to find.

    Returns:
        ShoppingListModel or dict: The found shopping list or an error message if not found.
    """
    try:
        shopping_list = ShoppingListModel.get(ShoppingListModel.id == shopping_list_id)  # Find shopping list by ID
        return shopping_list  # Return the found shopping list
    except ShoppingListModel.DoesNotExist:  # Handle case where the shopping list does not exist
        return {"error": "Shopping list not found"}  # Return an error message

def create_shopping_list(shopping_list: ShoppingList):
    """Create a new shopping list in the database.

    Args:
        shopping_list (ShoppingList): The shopping list object with new list information.

    Returns:
        ShoppingList: The created shopping list.
    """
    ShoppingListModel.create(
        user_id=shopping_list.user_id,
        created_at=shopping_list.created_at,
    )
    return shopping_list  # Return the created shopping list

def update_shopping_list(shopping_list_id: int, shopping_list: ShoppingList):
    """Update an existing shopping list.

    Args:
        shopping_list_id (int): The ID of the shopping list to update.
        shopping_list (ShoppingList): The shopping list object with updated information.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        ShoppingListModel.update(
            {
                ShoppingListModel.user_id: shopping_list.user_id,
                ShoppingListModel.created_at: shopping_list.created_at,
            }
        )
        .where(ShoppingListModel.id == shopping_list_id)  # Filter by ID
        .execute()  # Execute the update
    )

    if updated_rows == 0:  # Check if any rows were updated
        return {"error": "Shopping list not found"}  # Return an error message
    return {"message": "Shopping list updated successfully"}  # Return a success message

def delete_shopping_list(shopping_list_id: int):
    """Delete a shopping list by its ID.

    Args:
        shopping_list_id (int): The ID of the shopping list to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        shopping_list = ShoppingListModel.get(ShoppingListModel.id == shopping_list_id)  # Find shopping list by ID
        shopping_list.delete_instance()  # Delete the found shopping list
    except ShoppingListModel.DoesNotExist:  # Handle case where the shopping list does not exist
        return {"error": "Shopping list not found"}  # Return an error message
    return {"message": "Shopping list deleted successfully"}  # Return a success message

