from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.student import Student
from app.models.fee_payment import FeePayment

from app.schemas.fees.fee_payment import FeePaymentCreate

router = APIRouter(
    prefix="/fee-payments",
    tags=["Fee Payments"],
)


@router.post("/")
def collect_fee(
    payment: FeePaymentCreate,
    db: Session = Depends(get_db),
):
    student = (
        db.query(Student)
        .filter(Student.roll_number == payment.roll_number)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    total_paid = sum(
        p.amount for p in student.payments
    )

    pending_amount = student.total_fees - total_paid

    if payment.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero.",
        )

    new_payment = FeePayment(
        roll_number=payment.roll_number,
        amount=payment.amount,
        payment_method=payment.payment_method,
        payment_date=payment.payment_date,
        received_by = payment.received_by,
        remarks=payment.remarks,
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return {
        "success": True,
        "message": "Fees collected successfully.",
        "payment": new_payment,
    }