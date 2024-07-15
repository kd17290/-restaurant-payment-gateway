from models.customer_session import CustomerSession
from repositories.in_memory_repository import InMemoryRepository


class CustomerSessionRepository(InMemoryRepository[CustomerSession]):
    pass
