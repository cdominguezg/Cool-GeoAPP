class InvalidDateException(Exception):
    def __init__(self):
        super().__init__("Invalid dates")
