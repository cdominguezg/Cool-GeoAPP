from src.postal_code.domain.PostalCodeFeatures import PostalCodeFeatures
from src.postal_code.domain.PostalCodeType import PostalCodeType
from src.shared.domain.AggregateRoot import AggregateRoot


class PostalCode(AggregateRoot):

    def __init__(self,
                 geometry: PostalCodeFeatures,
                 type: PostalCodeType,
                 properties: dict):
        self.__geometry = geometry
        self.__type = type
        self.__properties = properties

    def to_primitives(self):
        return {
            'geometry': self.__geometry.value(),
            'type': self.__type.value(),
            'properties': self.__properties
        }
