from datetime import datetime

from pydantic import BaseModel


class FeePaymentResponse(BaseModel):
    id: int
    roll_number: str
    amount: float
    payment_date: datetime
    payment_method: str
    remarks: str | None
    received_by: str | None
    created_at: datetime
    class Config:
        from_attributes = True