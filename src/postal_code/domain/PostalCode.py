from src.postal_code.domain.PostalCodeFeatures import PostalCodeFeatures
from src.postal_code.domain.PostalCodeType import PostalCodeType
from src.shared.domain.AggregateRoot import AggregateRoot


class PostalCode(AggregateRoot):

    def __init__(self,
                 features: PostalCodeFeatures,
                 type: PostalCodeType):
        self.__features = features
        self.__type = type

    def to_primitives(self):
        return {
            'features': self.__features.value(),
            'type': self.__type.value()
        }
