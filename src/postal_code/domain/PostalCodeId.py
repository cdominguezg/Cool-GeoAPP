from src.shared.domain.ValueObject import ValueObject


class PostalCodeId(ValueObject):
    def __init__(self, value: int):
        super().__init__(value)
