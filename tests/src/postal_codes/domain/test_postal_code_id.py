from src.postal_code.domain.PostalCodeId import PostalCodeId


def test_postal_code_id():
    postal_code_id = PostalCodeId(1)
    assert postal_code_id.value() == 1
