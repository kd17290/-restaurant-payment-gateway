from models.base_model import BaseModel
from models.customer_session import CustomerSession


class Bill(BaseModel):
    customer_session: CustomerSession
    total_amount: float
    gst: float
    service_charge: float
    currency: str

    def __init__(
        self,
        customer_session: CustomerSession,
        total_amount: float,
        gst: float,
        service_charge: float,
        currency: str = "INR",
        id: int | None = None,
    ):
        super().__init__(id)
        self.customer_session = customer_session
        self.total_amount = total_amount
        self.gst = gst
        self.service_charge = service_charge
        self.currency = currency
