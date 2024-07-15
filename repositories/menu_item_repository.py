from models.menu_item import MenuItem
from repositories.in_memory_repository import InMemoryRepository


class MenuItemRepository(InMemoryRepository[MenuItem]):
    pass
