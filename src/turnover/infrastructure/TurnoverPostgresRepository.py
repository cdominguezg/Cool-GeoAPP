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

    def get_by_age_range(self, init_date, end_date):
        result = self.__client.execute_aggregated_query(query="""
                select jsonb_object_agg(age_range, json_build_object(
                'male', (
                    SELECT sum(amount)
                    from paystat t1
                    where t.age_range = t1.age_range and gender = 'M' and (month::date between '2015-01-01' and '2015-02-01')
                ),
                'female', (
                    SELECT sum(amount)
                    from paystat t1
                    where t.age_range = t1.age_range and gender = 'F' and (month::date between '2015-01-01' and '2015-02-01')
                )
            ))
        from (select age_range
              from paystat p
            where month::date between '2015-01-01' and '2015-02-01'
             ) t
        """, params={})
        return result.get('jsonb_object_agg') if result is not None else None
