from fastapi import FastAPI

from controllers.payment_controller import PaymentController
from models.bill import Bill
from models.customer_session import CustomerSession
from models.customer_session_status import CustomerSessionStatus
from models.payment import Payment
from models.user import User
from models.user_type import UserType
from repositories.bill_repository import BillRepository
from services.payment_service import PaymentService
from strategy.paytm_payment_gateway import PaytmPaymentGateway

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/make-payment/{bill_id}")
async def say_hello(bill_id: int):
    user = User(
        name="customer name",
        email="<EMAIL>",
        phone="1234567890",
        user_type=UserType.CUSTOMER,
    )
    customer_session = CustomerSession(
        user=user, customer_session_status=CustomerSessionStatus.ENDED
    )
    bill = Bill(
        customer_session=customer_session,
        total_amount=1000,
        gst=20,
        service_charge=10,
        currency="INR",
    )
    bill_repository = BillRepository()
    bill_repository.create(bill)
    paytm_gateway = PaytmPaymentGateway("1234567890", "123456")
    payment_service = PaymentService(paytm_gateway)
    payment: Payment = PaymentController(payment_service).make_payment(bill_id=bill_id)
    return {
        "id": payment.id,
        "txn": payment.txn,
        "bill_id": bill_id,
        "status": payment.payment_status,
        "amount": payment.amount,
    }
