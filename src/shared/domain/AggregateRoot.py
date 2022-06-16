from abc import ABC, abstractmethod


class AggregateRoot(ABC):

    @abstractmethod
    def to_primitives(self):
        raise NotImplementedError
