import abc
from abc import ABC


class Sort(ABC):
    sorting_object = None
    def __init__(self):
        pass

    @abc.abstractmethod
    def sort(self, arr):
        pass

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
