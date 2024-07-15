from models.bill import Bill
from repositories.bill_repository import BillRepository
from repositories.payment_repository import PaymentRepository
from strategy.payment_gateway import PaymentGateway


class PaymentService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.bill_repository = BillRepository()
        self.payment_repository = PaymentRepository()
        self.payment_gateway = payment_gateway

    def make_payment(self, bill_id: int):
        bill: Bill = self.bill_repository.find_by_id(bill_id)
        payment = self.payment_gateway.make_payment(
            bill_id, bill.total_amount, bill.currency
        )
        payment = self.payment_repository.create(payment)
        return payment
