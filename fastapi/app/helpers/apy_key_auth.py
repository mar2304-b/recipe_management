"""
api key helper
"""

# pylint: disable=import-error
import os

# pylint: disable=import-error
from dotenv import load_dotenv

# pylint: disable=import-error
from fastapi import HTTPException, Security, status

# pylint: disable=import-error
from fastapi.security.api_key import APIKeyHeader

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener la clave API de las variables de entorno
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

# Definir el encabezado de la clave API
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: str = Security(api_key_header)):
    """
    Verifica la clave API proporcionada en el encabezado de la solicitud.

    Args:
        api_key_header (str): La clave API proporcionada en el encabezado.

    Returns:
        str: La clave API si es válida.

    Raises:
        HTTPException: Si la clave API no es válida, se lanza una excepción
        con el código de estado 403.
    """
    if api_key == API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "status": False,
            "status_code": status.HTTP_403_FORBIDDEN,
            "message": "Unauthorized",
        },
    )