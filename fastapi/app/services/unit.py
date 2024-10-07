from config.database import UnitModel  # Importa el modelo de unidad
from models.unit import Unit  # Importa la clase Unit

def get_all_units():
    """Obtiene todas las unidades de la base de datos."""
    units = UnitModel.select().dicts()  # Selecciona todas las unidades como diccionarios
    return list(units)  # Retorna la lista de unidades

def get_unit_by_id(unit_id: int):
    """Obtiene una unidad por su ID.

    Args:
        unit_id (int): El ID de la unidad a buscar.

    Returns:
        UnitModel: La unidad encontrada o un mensaje de error si no existe.
    """
    try:
        unit = UnitModel.get(UnitModel.id == unit_id)  # Busca la unidad por ID
        return unit  # Retorna la unidad encontrada
    except UnitModel.DoesNotExist:  # Captura si la unidad no existe
        return {"error": "Unit not found"}  # Retorna un mensaje de error

def create_unit(unit: Unit):
    """Crea una nueva unidad en la base de datos.

    Args:
        unit (Unit): El objeto unidad con la información de la nueva unidad.

    Returns:
        Unit: La unidad creada.
    """
    UnitModel.create(
        name=unit.name,
    )
    return unit  # Retorna la unidad creada

def update_unit(unit_id: int, unit: Unit):
    """Actualiza una unidad existente.

    Args:
        unit_id (int): El ID de la unidad a actualizar.
        unit (Unit): El objeto unidad con la nueva información.

    Returns:
        dict: Mensaje de éxito o error.
    """
    updated_rows = (
        UnitModel.update(
            {
                UnitModel.name: unit.name,
            }
        )
        .where(UnitModel.id == unit_id)  # Filtra por ID
        .execute()  # Ejecuta la actualización
    )

    if updated_rows == 0:  # Verifica si se actualizó algún registro
        return {"error": "Unit not found"}  # Retorna un mensaje de error
    return {"message": "Unit updated successfully"}  # Retorna un mensaje de éxito

def delete_unit(unit_id: int):
    """Elimina una unidad por su ID.

    Args:
        unit_id (int): El ID de la unidad a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        unit = UnitModel.get(UnitModel.id == unit_id)  # Busca la unidad por ID
        unit.delete_instance()  # Elimina la unidad encontrada
    except UnitModel.DoesNotExist:  # Captura si la unidad no existe
        return {"error": "Unit not found"}  # Retorna un mensaje de error
    return {"message": "Unit deleted successfully"}  # Retorna un mensaje de éxito
