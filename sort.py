import abc
from abc import ABC


class Sort(ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def sort(self, arr):
        pass
