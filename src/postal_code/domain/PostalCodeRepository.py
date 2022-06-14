from abc import ABC

from src.postal_code.domain.PostalCodeId import PostalCodeId


class PostalCodeRepository(ABC):

    def list(self):
        pass

    def get(self, postal_code_id: PostalCodeId):
        pass
