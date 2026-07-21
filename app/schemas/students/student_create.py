from pydantic import BaseModel
from datetime import date
from ..fees.fee_payment import FeePaymentCreate


class StudentCreate(BaseModel):
    roll_number: int
    name: str
    gender: str
    dob: date
    phone: str
    email: str | None = None
    address: str
    father_name: str
    parents_phone: str
    course: str
    batch_time: str
    joining_date: date
    total_fees: float
    student_status:str
    payments: list[FeePaymentCreate] = []