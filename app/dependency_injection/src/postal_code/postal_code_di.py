from dependency_injector import containers, providers

from src.postal_code.application.PostalCodeLister import PostalCodeLister
from src.postal_code.infrastructure.PostalCodePostgresRepository import PostalCodePostgresRepository
from src.shared.infrastructure.PostgresClient import PostgresClient


class PostalCodeContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    postgres_sql_client = providers.Factory(
        PostgresClient,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        db_name=config.POSTGRES_DB_NAME
    )

    postal_code_repository = providers.Resource(
        PostalCodePostgresRepository,
        client=postgres_sql_client
    )

    postal_code_list_use_case = providers.Resource(
        PostalCodeLister,
        repository=postal_code_repository
    )
