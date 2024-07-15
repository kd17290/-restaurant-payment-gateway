from models.bill import Bill
from repositories.in_memory_repository import InMemoryRepository


class BillRepository(InMemoryRepository[Bill]):
    pass
