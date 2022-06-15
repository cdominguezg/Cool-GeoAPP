from dependency_injector import containers, providers

from src.shared.infrastructure.PostgresClient import PostgresClient
from src.turnover.application.TurnoverTotal import TurnoverTotal
from src.turnover.infrastructure.TurnoverPostgresRepository import TurnoverPostgresRepository


class TurnoverContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    postgres_sql_client = providers.Factory(
        PostgresClient,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        db_name=config.POSTGRES_DB_NAME
    )

    turnover_repository = providers.Resource(
        TurnoverPostgresRepository,
        client=postgres_sql_client
    )

    turnover_total_use_case = providers.Resource(
        TurnoverTotal,
        repository=turnover_repository
    )

