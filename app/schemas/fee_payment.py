from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FeePaymentCreate(BaseModel):

    amount: float

    payment_date: datetime

    payment_method: str = "Cash"

    remarks: Optional[str] = None

    received_by: Optional[str] = None