"""
API Key Helper Module
"""

# pylint: disable=import-error
import os

# pylint: disable=import-error
from dotenv import load_dotenv

# pylint: disable=import-error
from fastapi import HTTPException, Security, status

# pylint: disable=import-error
from fastapi.security.api_key import APIKeyHeader

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

# Define the API key header
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: str = Security(api_key_header)) -> str:
    """
    Verify the API key provided in the request header.

    Args:
        api_key (str): The API key provided in the header.

    Returns:
        str: The API key if it is valid.

    Raises:
        HTTPException: If the API key is invalid, raises an exception
        with a status code of 403.
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
