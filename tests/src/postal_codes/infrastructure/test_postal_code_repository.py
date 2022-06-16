import pytest

from src.postal_code.domain.PostalCode import PostalCode
from src.postal_code.domain.PostalCodeCollection import PostalCodeCollection
from src.postal_code.domain.PostalCodeId import PostalCodeId
from src.postal_code.infrastructure.PostalCodePostgresRepository import PostalCodePostgresRepository
from src.shared.infrastructure.PostgresClient import PostgresClient


@pytest.fixture(scope="module")
def repository():
    return PostalCodePostgresRepository(
        PostgresClient.create_client(
            host='localhost',
            port=5432,
            password='mysupersecretpassword',
            db_name='coolgeoapp',
            user='postgres'
        )
    )


def test_get_repository_method(repository):
    result = repository.get(postal_code_id=PostalCodeId(6055))
    assert type(result) == PostalCode
    result = repository.get(postal_code_id=PostalCodeId(1))
    assert result is None


def test_list_repository_method(repository):
    result = repository.list()
    assert type(result) == PostalCodeCollection
