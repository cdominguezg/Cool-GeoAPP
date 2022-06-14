from src.shared.domain.ValueObject import ValueObject


class PostalCodeType(ValueObject):
    def __init__(self, value: int):
        super().__init__(value)
