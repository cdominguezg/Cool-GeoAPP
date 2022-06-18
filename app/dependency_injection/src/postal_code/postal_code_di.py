from dependency_injector import containers, providers

from src.postal_code.application.PostalCodeFinder import PostalCodeFinder
from src.postal_code.application.PostalCodeLister import PostalCodeLister
from src.postal_code.infrastructure.PostalCodePostgresRepository import PostalCodePostgresRepository
from src.shared.infrastructure.PostgresClient import PostgresClient
from src.shared.infrastructure.RedisClient import RedisClient


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
    redis_client = providers.Factory(
        RedisClient,
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=1
    )

    postal_code_repository = providers.Resource(
        PostalCodePostgresRepository,
        client=postgres_sql_client,
        redis_client=redis_client
    )

    postal_code_list_use_case = providers.Resource(
        PostalCodeLister,
        repository=postal_code_repository
    )

    postal_code_finder_use_case = providers.Resource(
        PostalCodeFinder,
        repository=postal_code_repository
    )
