from models.family import FamilyModel
from services.family import (
    get_all_families,
    get_family_by_id,
    create_family,
    update_family,
    delete_family,
)
from fastapi import APIRouter

family_router = APIRouter()

@family_router.get("/")
def get_families():
    """
    Obtiene todas las familias.

    Returns:
        list: Lista de familias.
    """
    return get_all_families()

@family_router.get("/{id}")
def get_family(family_id: int):
    """
    Obtiene una familia específica por su ID.

    Args:
        family_id (int): ID de la familia a obtener.

    Returns:
        FamilyModel or dict: La familia si se encuentra, o un diccionario de error.
    """
    return get_family_by_id(family_id)

@family_router.post("/")
def register_family(family: FamilyModel):
    """
    Registra una nueva familia.

    Args:
        family (FamilyModel): Objeto de familia con los detalles a crear.

    Returns:
        FamilyModel: La familia creada.
    """
    return create_family(family)

@family_router.put("/{id}")
def update_family_data(family_id: int, family: FamilyModel):
    """
    Actualiza los datos de una familia existente.

    Args:
        family_id (int): ID de la familia a actualizar.
        family (FamilyModel): Objeto de familia con los nuevos detalles.

    Returns:
        dict: Mensaje de éxito o error.
    """
    return update_family(family_id, family)

@family_router.delete("/{id}")
def remove_family(family_id: int):
    """
    Elimina una familia de la base de datos.

    Args:
        family_id (int): ID de la familia a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    return delete_family(family_id)
