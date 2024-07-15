from exceptions import NotAuthenticated
from models.payment import Payment
from models.payment_status import PaymentStatus
from strategy.payment_gateway import PaymentGateway


class ApplePay(PaymentGateway):
    is_authenticated: bool = False

    def __init__(self, apple_id: str):
        self.apple_id = apple_id
        self.authenticate()

    def authenticate(self):
        self.is_authenticated = True

    def make_payment(self, bill_id: int, amount: float, currency: str) -> Payment:
        if not self.is_authenticated:
            raise NotAuthenticated("Not authenticated")
        return Payment(bill_id, amount, currency, PaymentStatus.COMPLETED)
