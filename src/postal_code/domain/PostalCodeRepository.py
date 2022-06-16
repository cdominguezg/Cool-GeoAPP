from abc import ABC

from src.postal_code.domain.PostalCodeId import PostalCodeId


class PostalCodeRepository(ABC):

    def list_geojson(self):
        pass

    def get_geojson(self, postal_code_id: PostalCodeId):
        pass
