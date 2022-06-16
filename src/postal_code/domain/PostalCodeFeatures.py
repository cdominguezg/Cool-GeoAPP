from src.shared.domain.ValueObject import ValueObject


class PostalCodeFeatures(ValueObject):
    def __init__(self, value):
        super().__init__(value)
