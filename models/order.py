from typing import Tuple

from models.base_model import BaseModel
from models.customer_session import CustomerSession
from models.menu_item import MenuItem


class Order(BaseModel):
    customer_session: CustomerSession
    order_items: Tuple[MenuItem, int]

    def __init__(
        self,
        customer_session: CustomerSession,
        order_items: Tuple[MenuItem, int],
        id: int | None = None,
    ):
        super().__init__(id)
        self.customer_session = customer_session
        self.order_items = order_items
