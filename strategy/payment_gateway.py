from abc import ABC, abstractmethod

from models.payment import Payment


class PaymentGateway(ABC):
    @abstractmethod
    def make_payment(self, bill_id: int, amount: float, currency: str) -> Payment:
        pass
