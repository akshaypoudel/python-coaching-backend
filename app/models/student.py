from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from ..database import Base

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    roll_number = Column(String(30), unique=True, nullable=False)

    name = Column(String(100), nullable=False)

    father_name = Column(String(100))

    parents_phone = Column(String(20))

    phone = Column(String(20))

    email = Column(String(100))

    gender = Column(String(20))

    dob = Column(Date)

    address = Column(String(255))

    batch_time = Column(String(50))

    joining_date = Column(Date)

    course = Column(String(100))

    total_fees = Column(Float)

    student_status = Column(String(20))
    payments = relationship(
    "FeePayment",
    back_populates="student",
    cascade="all, delete-orphan",
)
