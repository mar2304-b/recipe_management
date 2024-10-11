from config.database import MenuModel
from models.menu import Menu

def get_all_menus():
    """Retrieve all menus from the database.

    Returns:
        list: A list of menus as dictionaries.
    """
    menus = MenuModel.select().dicts()
    return list(menus)

def get_menu_by_id(menu_id: int):
    """Retrieve a specific menu by its ID.

    Args:
        menu_id (int): The ID of the menu to retrieve.

    Returns:
        Menu or dict: The menu if found, or an error dictionary.
    """
    try:
        menu = MenuModel.get(MenuModel.id == menu_id)
        return menu
    except MenuModel.DoesNotExist:
        return {"error": "Menu not found"}

def create_menu(menu: Menu):
    """Create a new menu in the database.

    Args:
        menu (Menu): Menu object containing details to create.

    Returns:
        Menu: The created menu object.
    """
    menu_instance = MenuModel.create(
        user_id=menu.user_id,
        menu_date=menu.menu_date,
        meal_type=menu.meal_type,
        create_at=menu.create_at,
    )
    return menu_instance

def update_menu(menu_id: int, menu: Menu):
    """Update an existing menu.

    Args:
        menu_id (int): The ID of the menu to update.
        menu (Menu): Menu object containing updated details.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        MenuModel.update(
            {
                MenuModel.user_id: menu.user_id,
                MenuModel.menu_date: menu.menu_date,
                MenuModel.meal_type: menu.meal_type,
                MenuModel.create_at: menu.create_at,
            }
        )
        .where(MenuModel.id == menu_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Menu not found"}
    return {"message": "Menu updated successfully"}

def delete_menu(menu_id: int):
    """Delete a menu from the database.

    Args:
        menu_id (int): The ID of the menu to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        menu = MenuModel.get(MenuModel.id == menu_id)
        menu.delete_instance()
    except MenuModel.DoesNotExist:
        return {"error": "Menu not found"}
    return {"message": "Menu deleted successfully"}

