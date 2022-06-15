from abc import ABC
from typing import TypeVar

T = TypeVar("T")


class ValueObject(ABC):
    __value = None

    def __init__(self, value: T):
        self.__value = value

    def value(self):
        return self.__value

    def __eq__(self, other: 'ValueObject'):
        return self.value() == other.value()

    def __str__(self):
        return str(self.__value)
