from models.base_model import BaseModel
from .user_type import UserType


class User(BaseModel):
    name: str
    email: str
    phone: str
    user_type: UserType

    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        user_type: UserType = UserType.CUSTOMER,
        id: int | None = None,
    ):
        super().__init__(id)
        self.name = name
        self.email = email
        self.phone = phone
        self.user_type = user_type
        self.id = id
