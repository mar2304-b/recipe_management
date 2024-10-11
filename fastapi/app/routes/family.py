from models.family import Family
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
    Retrieve all families.

    Returns:
        list: A list of all families.
    """
    return get_all_families()

@family_router.get("/{family_id}")
def get_family(family_id: int):
    """
    Retrieve a specific family by its ID.

    Args:
        family_id (int): The ID of the family to retrieve.

    Returns:
        Family or dict: The family if found, or an error dictionary.
    """
    return get_family_by_id(family_id)

@family_router.post("/")
def register_family(family: Family):
    """
    Register a new family.

    Args:
        family (Family): Family object containing details for the new family.

    Returns:
        Family: The created family object.
    """
    return create_family(family)

@family_router.put("/{family_id}")
def update_family_data(family_id: int, family: Family):
    """
    Update the data of an existing family.

    Args:
        family_id (int): The ID of the family to update.
        family (Family): Family object containing updated details.

    Returns:
        dict: A message indicating success or error.
    """
    return update_family(family_id, family)

@family_router.delete("/{family_id}")
def remove_family(family_id: int):
    """
    Delete a family from the database.

    Args:
        family_id (int): The ID of the family to delete.

    Returns:
        dict: A message indicating success or error.
    """
    return delete_family(family_id)

