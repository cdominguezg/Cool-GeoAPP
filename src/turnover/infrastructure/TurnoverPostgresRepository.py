from src.shared.infrastructure.PostgresClient import PostgresClient
from src.turnover.domain.TurnoverRepository import TurnoverRepository


class TurnoverPostgresRepository(TurnoverRepository):

    def __init__(self,
                 client: PostgresClient):
        self.__client = client

    def get_total(self, init_date, end_date):
        result = self.__client.execute_aggregated_query(query=
                                                        'select sum(amount) as "total" from paystat where month::date between %(init_date)s and %(end_date)s',
                                                        params={
                                                            "init_date": init_date,
                                                            "end_date": end_date
                                                        })
        return result
