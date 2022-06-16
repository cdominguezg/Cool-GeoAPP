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
                    where t.age_range = t1.age_range and gender = 'M' and (month::date between %(init_date)s and %(end_date)s)
                ),
                'female', (
                    SELECT sum(amount)
                    from paystat t1
                    where t.age_range = t1.age_range and gender = 'F' and (month::date between %(init_date)s and %(end_date)s)
                )
            ))
        from (select age_range
              from paystat p
            where month::date between %(init_date)s and %(end_date)s
             ) t
        """, params={
            "init_date": init_date,
            "end_date": end_date
        })
        return result.get('jsonb_object_agg') if result is not None else None

    def get_by_date(self, init_date, end_date):
        result = self.__client.execute_aggregated_query(query="""
                    select jsonb_object_agg(t.month, (select array_to_json(array_agg(row_to_json(a)))
                                              from (
                                                       select age_range, gender, sum(amount) as "total"
                                                       from paystat
                                                       where month = t.month
                                                       group by age_range, gender
                                                       order by age_range, gender
                                                   ) a))
            
            from (select month
                  from paystat p
                  where month::date between %(init_date)s and %(end_date)s order by month
                 ) t;
        """, params={
            "init_date": init_date,
            "end_date": end_date
        })
        return result.get('jsonb_object_agg') if result is not None else None
