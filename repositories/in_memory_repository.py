from typing import Generic, TypeVar

from singleton import Singleton

T = TypeVar("T")


class InMemoryRepository(Generic[T], metaclass=Singleton["InMemoryRepository"]):
    def __init__(self):
        self._data = {}
        self.counter = 1

    def find_by_id(self, pk: int) -> T:
        return self._data.get(pk, None)

    def create(self, obj: T) -> T:
        obj.id = self.counter
        self._data[obj.id] = obj
        self.counter += 1
        return obj
