from config.database import MenuModel
from models.menu import Menu

def get_all_menus():
    """
    Obtiene todos los menús de la base de datos.

    Returns:
        list: Lista de menús como diccionarios.
    """
    menus = MenuModel.select().dicts()
    return list(menus)

def get_menu_by_id(menu_id: int):
    """
    Obtiene un menú específico por su ID.

    Args:
        menu_id (int): ID del menú a obtener.

    Returns:
        Menu or dict: El menú si se encuentra, o un diccionario de error.
    """
    try:
        menu = MenuModel.get(MenuModel.id == menu_id)
        return menu
    except MenuModel.DoesNotExist:
        return {"error": "Menu not found"}

def create_menu(menu: Menu):
    """
    Crea un nuevo menú en la base de datos.

    Args:
        menu (Menu): Objeto de menú con los detalles a crear.

    Returns:
        Menu: El menú creado.
    """
    MenuModel.create(
        user_id=menu.user_id,
        menu_date=menu.menu_date,
        meal_type=menu.meal_type,
        created_at=menu.created_at,
    )
    return menu

def update_menu(menu_id: int, menu: Menu):
    """
    Actualiza un menú existente.

    Args:
        menu_id (int): ID del menú a actualizar.
        menu (Menu): Objeto de menú con los nuevos detalles.

    Returns:
        dict: Mensaje de éxito o error.
    """
    updated_rows = (
        MenuModel.update(
            {
                MenuModel.user_id: menu.user_id,
                MenuModel.menu_date: menu.menu_date,
                MenuModel.meal_type: menu.meal_type,
                MenuModel.created_at: menu.created_at,
            }
        )
        .where(MenuModel.id == menu_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Menu not found"}
    return {"message": "Menu updated successfully"}

def delete_menu(menu_id: int):
    """
    Elimina un menú de la base de datos.

    Args:
        menu_id (int): ID del menú a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        menu = MenuModel.get(MenuModel.id == menu_id)
        menu.delete_instance()
    except MenuModel.DoesNotExist:
        return {"error": "Menu not found"}
    return {"message": "Menu deleted successfully"}
