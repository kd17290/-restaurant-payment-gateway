from models.base_model import BaseModel
from models.dietary_type import DietaryType
from models.item_type import ItemType


class MenuItem(BaseModel):
    name: str
    description: str
    amount: float
    item_type: ItemType
    dietary_type: DietaryType

    def __init__(
        self,
        name: str,
        description: str,
        amount: float,
        item_type: ItemType,
        dietary_type: DietaryType,
        id: int | None = None,
    ):
        super().__init__(id)
        self.name = name
        self.description = description
        self.amount = amount
        self.item_type = item_type
        self.dietary_type = dietary_type
