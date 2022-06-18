from src.postal_code.domain.PostalCodeId import PostalCodeId
from src.postal_code.domain.PostalCodeRepository import PostalCodeRepository


class PostalCodeFinder:

    def __init__(self, repository: PostalCodeRepository):
        self.repository = repository

    def run(self, id: int):
        return self.repository.get_geojson(PostalCodeId(id)) or None
