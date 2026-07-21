from app.schemas.fees.fee_payment_response import FeePaymentResponse
from pydantic import BaseModel
from datetime import date


class StudentResponse(BaseModel):
    roll_number: str
    name: str
    gender: str
    dob: date
    phone: str
    email: str | None
    address: str
    father_name: str
    parents_phone: str
    course: str
    batch_time: str
    joining_date: date
    total_fees: float
    student_status: str
    payments:list[FeePaymentResponse] = []
    class Config:
        from_attributes = True