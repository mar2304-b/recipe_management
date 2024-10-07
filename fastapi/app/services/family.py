from config.database import FamilyModel
from models.family import Family

def get_all_families():
    """
    Obtiene todas las familias de la base de datos.

    Returns:
        list: Lista de familias como diccionarios.
    """
    families = FamilyModel.select().dicts()
    return list(families)

def get_family_by_id(family_id: int):
    """
    Obtiene una familia específica por su ID.

    Args:
        family_id (int): ID de la familia a obtener.

    Returns:
        Family or dict: La familia si se encuentra, o un diccionario de error.
    """
    try:
        family = FamilyModel.get(FamilyModel.id == family_id)
        return family
    except FamilyModel.DoesNotExist:
        return {"error": "Family not found"}

def create_family(family: Family):
    """
    Crea una nueva familia en la base de datos.

    Args:
        family (Family): Objeto de familia con los detalles a crear.

    Returns:
        Family: La familia creada.
    """
    FamilyModel.create(
        name=family.name,
    )
    return family

def update_family(family_id: int, family: Family):
    """
    Actualiza una familia existente.

    Args:
        family_id (int): ID de la familia a actualizar.
        family (Family): Objeto de familia con los nuevos detalles.

    Returns:
        dict: Mensaje de éxito o error.
    """
    updated_rows = (
        FamilyModel.update(
            {
                FamilyModel.name: family.name,
            }
        )
        .where(FamilyModel.id == family_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Family not found"}
    return {"message": "Family updated successfully"}

def delete_family(family_id: int):
    """
    Elimina una familia de la base de datos.

    Args:
        family_id (int): ID de la familia a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        family = FamilyModel.get(FamilyModel.id == family_id)
        family.delete_instance()
    except FamilyModel.DoesNotExist:
        return {"error": "Family not found"}
    return {"message": "Family deleted successfully"}
