from src.shared.domain.ValueObject import ValueObject


class PostalCodeFeatures(ValueObject):
    def __init__(self, value: str):
        super().__init__(value)
