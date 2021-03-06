import json

from src.postal_code.domain.PostalCodeId import PostalCodeId
from src.postal_code.domain.PostalCodeRepository import PostalCodeRepository
from src.shared.infrastructure.PostgresClient import PostgresClient
from src.shared.infrastructure.RedisClient import RedisClient


class PostalCodePostgresRepository(PostalCodeRepository):

    def __init__(self,
                 client: PostgresClient,
                 redis_client: RedisClient):
        self.__client = client
        self.__redis_client = redis_client

    def list_geojson(self):
        if self.__redis_client.exists('postal_code_list_geojson'):
            return json.loads(self.__redis_client.get('postal_code_list_geojson'))
        result = self.__client.execute_aggregated_query(query="""
            SELECT jsonb_build_object(
               'type', 'FeatureCollection',
               'features', jsonb_agg(features.feature)
           ) as "geom"
FROM (
         SELECT jsonb_build_object(
                        'type', 'Feature',
                        'geometry', ST_AsGeoJSON(ST_Transform(geom, 4326))::jsonb,
                        'properties', json_build_object(
                                              'result', json_build_object(
                                                                'data', (
                                     select jsonb_object_agg(age_range, result)
                                     from (select ps.age_range,
                                         CONCAT((select CONCAT(gender, ' ', sum(t1.amount))
                                                 from paystat t1
                                                 where gender = 'M'
                                                   and t1.age_range = ps.age_range and t1.postal_code_id=inputs.id
                                                 group by t1.gender), ' ',
                                                (select CONCAT(gender, ' ', sum(t2.amount))
                                                 from paystat t2
                                                 where gender = 'F'
                                                   and t2.age_range = ps.age_range and t2.postal_code_id=inputs.id
                                                 group by t2.gender)) as "result"
                                  from paystat ps
                                  group by age_range
                                          ) t))::jsonb -> 'data' || json_build_object('zipcode', code)::jsonb) ->
                                      'result'
                    ) AS feature
         FROM (SELECT geom, code, id
               from postal_code p) inputs) features;
            """, params=None).get('geom')
        self.__redis_client.set('postal_code_list_geojson', json.dumps(result))
        return result

    def get_geojson(self, postal_code_id: PostalCodeId):
        if self.__redis_client.exists('postal_code_' + str(postal_code_id) + '_geojson'):
            return json.loads(self.__redis_client.get('postal_code_' + str(postal_code_id) + '_geojson'))
        result = self.__client.execute_aggregated_query(query="""
                    select json_build_object(
                       'type', 'Feature',
                       'geometry', ST_AsGeoJSON(ST_Transform(geom, 4326))::jsonb,
                       'properties', json_build_object(
                                             'result', json_build_object(
                                                               'data', (
                                    select jsonb_object_agg(age_range, result)
                                    from (select ps.age_range,
                                                 CONCAT((select CONCAT(gender, ' ', sum(t1.amount))
                                                         from paystat t1
                                                         where gender = 'M'
                                                           and t1.age_range = ps.age_range
                                                           and t1.postal_code_id = p.id
                                                         group by t1.gender), ' ',
                                                        (select CONCAT(gender, ' ', sum(t2.amount))
                                                         from paystat t2
                                                         where gender = 'F'
                                                           and t2.age_range = ps.age_range
                                                           and t2.postal_code_id = p.id
                                                         group by t2.gender)) as "result"
                                          from paystat ps
                                          group by age_range
                                         ) t))::jsonb -> 'data' || json_build_object('zipcode', code)::jsonb) ->
                                     'result'
                   ) as "geom"
                from postal_code p
                where id = %(id)s;
                    """, params={
            'id': postal_code_id.value()
        })
        result = result.get('geom') or None if result is not None else None
        if result is not None:
            self.__redis_client.set('postal_code_' + str(postal_code_id) + '_geojson', json.dumps(result))
        return result
