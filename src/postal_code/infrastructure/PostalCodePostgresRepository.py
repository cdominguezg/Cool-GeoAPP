from src.postal_code.domain.PostalCode import PostalCode
from src.postal_code.domain.PostalCodeFeatures import PostalCodeFeatures
from src.postal_code.domain.PostalCodeType import PostalCodeType
from src.postal_code.domain.PostalCodeRepository import PostalCodeRepository
from src.shared.infrastructure.PostgresClient import PostgresClient


class PostalCodePostgresRepository(PostalCodeRepository):

    def __init__(self,
                 client: PostgresClient):
        self.__client = client

    def list(self):
        result = self.__client.execute_json_query(query="""
            SELECT jsonb_build_object(
               'type', 'FeatureCollection',
               'features', jsonb_agg(features.feature)
           ) as "geom"
            FROM (
                 SELECT jsonb_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(geom)::jsonb,
                                'properties', json_build_object(
                                            'result',json_build_object(
                                            'data', (
                                                    select jsonb_object_agg(age_range, concat(gender,' ',total)) from (select age_range,gender,sum(amount) as total from paystat where postal_code_id = inputs.id group by age_range,gender
                                                    ) t))::jsonb -> 'data' || json_build_object('zipcode', code)::jsonb) -> 'result'
        
                            ) AS feature
                 FROM (SELECT geom, code, id
                    from postal_code) inputs) features;
            """, params=None).get('geom')
        return PostalCode(features=PostalCodeFeatures(result['features']),
                          type=PostalCodeType(result['type'])) if result is not None else None
