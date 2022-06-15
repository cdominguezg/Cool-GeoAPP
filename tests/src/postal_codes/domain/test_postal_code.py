from src.postal_code.domain.PostalCode import PostalCode
from src.postal_code.domain.PostalCodeFeatures import PostalCodeFeatures
from src.postal_code.domain.PostalCodeType import PostalCodeType


def test_postal_code_collection():
    postal_code = PostalCode(
        geometry=PostalCodeFeatures({"test": "test"}),
        type=PostalCodeType("Test"),
        properties={"test": "test"}
    )
    assert type(postal_code) == PostalCode
    assert postal_code.to_primitives() == {
        'geometry': {
            'test': 'test'
        },
        'type': "Test",
        'properties': {
            'test': 'test'
        },
    }
