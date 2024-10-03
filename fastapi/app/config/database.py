from peewee import *
from config.settings import DATABASE

print(DATABASE)

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)