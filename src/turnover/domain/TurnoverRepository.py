from abc import ABC



class TurnoverRepository(ABC):

    def get_total(self, init_date, end_date):
        pass

    def get_by_age_range(self, init_date, end_date):
        pass