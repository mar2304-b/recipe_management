from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Configuración de Alembic.
# Accede a los valores del archivo .ini en uso.
config = context.config

# Configura los loggers según el archivo de configuración.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# MetaData del modelo para soporte de 'autogenerate'.
target_metadata = None

def run_migrations_offline() -> None:
    """Ejecuta migraciones en modo 'offline'.

    Configura el contexto solo con una URL, sin necesidad de un Engine.
    Las llamadas a context.execute() emiten la cadena dada al output del script.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Ejecuta migraciones en modo 'online'.

    Crea un Engine y asocia una conexión con el contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Ejecuta las migraciones según el modo (offline u online).
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()