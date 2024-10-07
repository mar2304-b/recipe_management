from config.database import ShoppingListModel  # Importa el modelo de lista de compras
from models.shopping_list import ShoppingList  # Importa la clase ShoppingList

def get_all_shopping_lists():
    """Obtiene todas las listas de compras de la base de datos."""
    shopping_lists = ShoppingListModel.select().dicts()  # Selecciona todas las listas de compras como diccionarios
    return list(shopping_lists)  # Retorna la lista de listas de compras

def get_shopping_list_by_id(shopping_list_id: int):
    """Obtiene una lista de compras por su ID.

    Args:
        shopping_list_id (int): El ID de la lista de compras a buscar.

    Returns:
        ShoppingListModel: La lista de compras encontrada o un mensaje de error si no existe.
    """
    try:
        shopping_list = ShoppingListModel.get(ShoppingListModel.id == shopping_list_id)  # Busca la lista de compras por ID
        return shopping_list  # Retorna la lista de compras encontrada
    except ShoppingListModel.DoesNotExist:  # Captura si la lista de compras no existe
        return {"error": "Shopping list not found"}  # Retorna un mensaje de error

def create_shopping_list(shopping_list: ShoppingList):
    """Crea una nueva lista de compras en la base de datos.

    Args:
        shopping_list (ShoppingList): El objeto lista de compras con la información de la nueva lista.

    Returns:
        ShoppingList: La lista de compras creada.
    """
    ShoppingListModel.create(
        user_id=shopping_list.user_id,
        created_at=shopping_list.created_at,
    )
    return shopping_list  # Retorna la lista de compras creada

def update_shopping_list(shopping_list_id: int, shopping_list: ShoppingList):
    """Actualiza una lista de compras existente.

    Args:
        shopping_list_id (int): El ID de la lista de compras a actualizar.
        shopping_list (ShoppingList): El objeto lista de compras con la nueva información.

    Returns:
        dict: Mensaje de éxito o error.
    """
    updated_rows = (
        ShoppingListModel.update(
            {
                ShoppingListModel.user_id: shopping_list.user_id,
                ShoppingListModel.created_at: shopping_list.created_at,
            }
        )
        .where(ShoppingListModel.id == shopping_list_id)  # Filtra por ID
        .execute()  # Ejecuta la actualización
    )

    if updated_rows == 0:  # Verifica si se actualizó algún registro
        return {"error": "Shopping list not found"}  # Retorna un mensaje de error
    return {"message": "Shopping list updated successfully"}  # Retorna un mensaje de éxito

def delete_shopping_list(shopping_list_id: int):
    """Elimina una lista de compras por su ID.

    Args:
        shopping_list_id (int): El ID de la lista de compras a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        shopping_list = ShoppingListModel.get(ShoppingListModel.id == shopping_list_id)  # Busca la lista de compras por ID
        shopping_list.delete_instance()  # Elimina la lista de compras encontrada
    except ShoppingListModel.DoesNotExist:  # Captura si la lista de compras no existe
        return {"error": "Shopping list not found"}  # Retorna un mensaje de error
    return {"message": "Shopping list deleted successfully"}  # Retorna un mensaje de éxito
