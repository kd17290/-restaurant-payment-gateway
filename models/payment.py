import uuid

from models.base_model import BaseModel
from models.bill import Bill
from models.payment_status import PaymentStatus


class Payment(BaseModel):
    bill_id: int
    amount: float
    currency: str
    payment_status: PaymentStatus
    txn: str

    def __init__(
        self,
        bill_id: int,
        amount: float,
        currency: str,
        payment_status: PaymentStatus = PaymentStatus.PENDING,
        id: int | None = None,
    ):
        super().__init__(id)
        self.bill_id = bill_id
        self.amount = amount
        self.currency = currency
        self.payment_status = payment_status
        self.txn = uuid.uuid4().hex
