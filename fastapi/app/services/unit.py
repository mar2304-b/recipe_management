from config.database import UnitModel  # Import the unit model
from models.unit import Unit  # Import the Unit class

def get_all_units():
    """Retrieve all units from the database.

    Returns:
        list: A list of units as dictionaries.
    """
    units = UnitModel.select().dicts()  # Select all units as dictionaries
    return list(units)  # Return the list of units

def get_unit_by_id(unit_id: int):
    """Retrieve a unit by its ID.

    Args:
        unit_id (int): The ID of the unit to find.

    Returns:
        UnitModel or dict: The found unit or an error message if not found.
    """
    try:
        unit = UnitModel.get(UnitModel.id == unit_id)  # Find the unit by ID
        return unit  # Return the found unit
    except UnitModel.DoesNotExist:  # Handle case where the unit does not exist
        return {"error": "Unit not found"}  # Return an error message

def create_unit(unit: Unit):
    """Create a new unit in the database.

    Args:
        unit (Unit): The unit object with new unit information.

    Returns:
        Unit: The created unit.
    """
    UnitModel.create(
        name=unit.name,
    )
    return unit  # Return the created unit

def update_unit(unit_id: int, unit: Unit):
    """Update an existing unit.

    Args:
        unit_id (int): The ID of the unit to update.
        unit (Unit): The unit object with updated information.

    Returns:
        dict: A message indicating success or error.
    """
    updated_rows = (
        UnitModel.update(
            {
                UnitModel.name: unit.name,
            }
        )
        .where(UnitModel.id == unit_id)  # Filter by ID
        .execute()  # Execute the update
    )

    if updated_rows == 0:  # Check if any rows were updated
        return {"error": "Unit not found"}  # Return an error message
    return {"message": "Unit updated successfully"}  # Return a success message

def delete_unit(unit_id: int):
    """Delete a unit by its ID.

    Args:
        unit_id (int): The ID of the unit to delete.

    Returns:
        dict: A message indicating success or error.
    """
    try:
        unit = UnitModel.get(UnitModel.id == unit_id)  # Find the unit by ID
        unit.delete_instance()  # Delete the found unit
    except UnitModel.DoesNotExist:  # Handle case where the unit does not exist
        return {"error": "Unit not found"}  # Return an error message
    return {"message": "Unit deleted successfully"}  # Return a success message
