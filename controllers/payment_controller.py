from services.payment_service import PaymentService


class PaymentController:
    payment_service = PaymentService

    def __init__(self, payment_service):
        self.payment_service = payment_service

    def make_payment(self, bill_id: int):
        return self.payment_service.make_payment(bill_id)
