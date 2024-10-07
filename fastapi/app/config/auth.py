# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime, timedelta

# # Configuración de JWT
# SECRET_KEY = "secret_key"  # Clave secreta para codificar el JWT
# ALGORITHM = "HS256"  # Algoritmo de codificación
# ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Tiempo de expiración del token en minutos

# # Configuración de contraseña
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Contexto para la encriptación de contraseñas

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # Estrategia de autenticación

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     """Verifica si la contraseña en texto plano coincide con la contraseña encriptada."""
#     return pwd_context.verify(plain_password, hashed_password)

# def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
#     """Crea un token de acceso JWT.

#     Args:
#         data (dict): Datos a incluir en el token.
#         expires_delta (timedelta, opcional): Tiempo de expiración del token.
    
#     Returns:
#         str: Token de acceso codificado.
#     """
#     to_encode = data.copy()  # Copia de los datos
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta  # Fecha de expiración personalizada
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)  # Fecha de expiración predeterminada
#     to_encode.update({"exp": expire})  # Añade la fecha de expiración a los datos
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Codifica el JWT
#     return encoded_jwt

# def auth_user(username: str, password: str):
#     """Autentica al usuario verificando las credenciales.

#     Args:
#         username (str): Nombre de usuario.
#         password (str): Contraseña.

#     Returns:
#         User: Usuario autenticado si es válido, de lo contrario, False.
#     """
#     user = get_user_from_db(username)  # Obtiene el usuario de la base de datos (simulado)
#     if not user or not verify_password(password, user.hashed_password):
#         return False  # Credenciales inválidas
#     return user  # Credenciales válidas

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     """Obtiene el usuario actual a partir del token JWT.

#     Args:
#         token (str): Token de acceso.

#     Raises:
#         HTTPException: Si el token es inválido.
    
#     Returns:
#         User: Usuario actual.
#     """
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Decodifica el token
#         username: str = payload.get("sub")  # Obtiene el nombre de usuario del payload
#         if username is None:
#             raise HTTPException(status_code=400, detail="Invalid token")  # Token inválido
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")  # Token inválido
