from datetime import datetime

from src.turnover.domain.InvalidDateException import InvalidDateException
from src.turnover.domain.TurnoverRepository import TurnoverRepository


class TurnoverByAge:
    def __init__(self, repository: TurnoverRepository):
        self.repository = repository

    def run(self, init_date, end_date):
        if datetime.strptime(init_date, '%Y-%m-%d') > datetime.strptime(end_date, '%Y-%m-%d'):
            raise InvalidDateException
        return self.repository.get_by_age_range(init_date, end_date)
