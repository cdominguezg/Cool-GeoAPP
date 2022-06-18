from dependency_injector import containers, providers

from src.shared.infrastructure.PostgresClient import PostgresClient
from src.shared.infrastructure.RedisClient import RedisClient
from src.turnover.application.TurnoverByAge import TurnoverByAge
from src.turnover.application.TurnoverByDate import TurnoverByDate
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

    redis_client = providers.Factory(
        RedisClient,
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=0
    )

    turnover_repository = providers.Resource(
        TurnoverPostgresRepository,
        client=postgres_sql_client,
        redis_client=redis_client
    )

    turnover_total_use_case = providers.Resource(
        TurnoverTotal,
        repository=turnover_repository
    )

    turnover_by_age_use_case = providers.Resource(
        TurnoverByAge,
        repository=turnover_repository
    )

    turnover_by_date_use_case = providers.Resource(
        TurnoverByDate,
        repository=turnover_repository
    )
