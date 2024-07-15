from exceptions import NotAuthenticated
from models.payment import Payment
from models.payment_status import PaymentStatus
from strategy.payment_gateway import PaymentGateway


class PaytmPaymentGateway(PaymentGateway):
    is_authenticated: bool = False

    def __init__(self, phone_number: str, otp: str):
        print("paytm gateway initialising")
        self.phone_number = phone_number
        self.otp = otp
        self.authenticate()

    def authenticate(self):
        print(f"authenticating via otp: {self.otp} for phone: {self.phone_number}")
        self.is_authenticated = True

    def make_payment(self, bill_id: int, amount: float, currency: str) -> Payment:
        print(f"making payment: {bill_id} {amount} {currency}")
        if not self.is_authenticated:
            raise NotAuthenticated("Not authenticated")
        return Payment(bill_id, amount, currency, PaymentStatus.COMPLETED)
