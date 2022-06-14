from abc import ABC

from src.postal_code.domain.PostalCodeType import PostalCodeType


class PostalCodeRepository(ABC):

    def list(self):
        pass

    def get(self, postal_code_id: PostalCodeType):
        pass
