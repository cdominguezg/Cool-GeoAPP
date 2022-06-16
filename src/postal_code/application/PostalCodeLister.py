from src.postal_code.domain.PostalCodeRepository import PostalCodeRepository


class PostalCodeLister:

    def __init__(self, repository: PostalCodeRepository):
        self.repository = repository

    def run(self):
        return self.repository.list()