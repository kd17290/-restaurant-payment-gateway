from abc import ABC


class BaseModel(ABC):
    id: int | None = None

    def __init__(self, id: int | None = None):
        self.id = id
