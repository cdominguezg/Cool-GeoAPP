from src.postal_code.domain.PostalCode import PostalCode
from src.postal_code.domain.PostalCodeFeatures import PostalCodeFeatures
from src.postal_code.domain.PostalCodeProperties import PostalCodeProperties
from src.postal_code.domain.PostalCodeType import PostalCodeType
from src.postal_code.infrastructure.PostalCodePostgresRepository import PostalCodePostgresRepository
from src.shared.infrastructure.PostgresClient import PostgresClient


class PostalCodeLister:

    def run(self):
        cliente = PostgresClient.create_client(host="localhost",
                                               port=5432,
                                               db_name="coolgeoapp",
                                               password="mysupersecretpassword",
                                               user="postgres")
        return PostalCodePostgresRepository(cliente).list()
