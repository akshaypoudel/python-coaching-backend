from sqlalchemy import (
    Column,
    Integer,
    String,
    Double,
    DateTime,
    Enum,
    ForeignKey,
    TIMESTAMP,
    text,
)
from sqlalchemy.orm import relationship

from ..database import Base


class FeePayment(Base):
    __tablename__ = "fee_payments"
    id = Column(Integer, primary_key=True, index=True)
    # Student Reference
    roll_number = Column(
        String(30),
        ForeignKey("students.roll_number", ondelete="CASCADE"),
        nullable=False,
    )
    # Payment Details
    amount = Column(Double, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    payment_method = Column(
        Enum("Cash", "Card", "UPI"),
        nullable=False,
        default="Cash",
    )
    remarks = Column(String(255), nullable=True)
    received_by = Column(String(50), nullable=True)
    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    # Relationship
    student = relationship(
        "Student",
        back_populates="payments",
    )