from config.database import FamilyModel
from models.family import Family

def get_all_families():
    """
    Retrieve all families from the database.

    Returns:
        list: A list of families as dictionaries.
    """
    families = FamilyModel.select().dicts()
    return list(families)

def get_family_by_id(family_id: int):
    """
    Retrieve a specific family by its ID.

    Args:
        family_id (int): The ID of the family to retrieve.

    Returns:
        Family or dict: The family if found, or an error dictionary.
    """
    try:
        family = FamilyModel.get(FamilyModel.id == family_id)
        return family
    except FamilyModel.DoesNotExist:
        return {"error": "Family not found"}

def create_family(family: Family):
    """
    Create a new family in the database.

    Args:
        family (Family): Family object containing details to create.

    Returns:
        Family: The created family object.
    """
    family_instance = FamilyModel.create(
        name=family.name,
    )
    return family_instance

def update_family(family_id: int, family: Family):
    """
    Update an existing family.

    Args:
        family_id (int): The ID of the family to update.
        family (Family): Family object containing updated details.

    Returns:
        dict: A message indicating success or error.
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
    Delete a family from the database.

    Args:
        family_id (int): The ID of the family to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        family = FamilyModel.get(FamilyModel.id == family_id)
        family.delete_instance()
    except FamilyModel.DoesNotExist:
        return {"error": "Family not found"}
    return {"message": "Family deleted successfully"}
