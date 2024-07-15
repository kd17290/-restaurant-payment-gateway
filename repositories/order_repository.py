from models.bill import Bill
from models.order import Order
from repositories.in_memory_repository import InMemoryRepository


class OrderRepository(InMemoryRepository[Order]):
    pass
