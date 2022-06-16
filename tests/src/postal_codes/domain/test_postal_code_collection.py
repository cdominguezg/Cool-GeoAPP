from src.postal_code.domain.PostalCodeCollection import PostalCodeCollection
from src.postal_code.domain.PostalCodeFeatures import PostalCodeFeatures
from src.postal_code.domain.PostalCodeType import PostalCodeType


def test_postal_code_collection():
    postal_code = PostalCodeCollection(
        features=PostalCodeFeatures({"test": "test"}),
        type=PostalCodeType("Test")
    )
    assert type(postal_code) == PostalCodeCollection
    assert postal_code.to_primitives() == {
        'features': {
            'test': 'test'
        },
        'type': "Test"
    }
