from datetime import datetime

from models.base_model import BaseModel
from models.customer_session_status import CustomerSessionStatus
from models.user import User


class CustomerSession(BaseModel):
    user: User
    start_time: datetime
    end_time: datetime
    customer_session_status: CustomerSessionStatus

    def __init__(
        self,
        user: User,
        customer_session_status: CustomerSessionStatus,
        id: int | None = None,
    ):
        super().__init__(id)
        self.user = user
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.customer_session_status = customer_session_status
