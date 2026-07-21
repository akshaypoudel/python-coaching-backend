from fastapi import HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import selectinload
from ..database import SessionLocal
from ..models.student import Student
from ..models.fee_payment import FeePayment
from ..schemas.students.student_create import StudentCreate
from ..schemas.students.student_response import StudentResponse

router = APIRouter()


@router.post(
    "/students",
    response_model=StudentResponse,
)
def add_student(data: StudentCreate):

    db = SessionLocal()

    try:

        existing_student = (db.query(Student).filter(Student.roll_number == data.roll_number).first())

        if existing_student:
            db.close()
            raise HTTPException(
                status_code=400,
                detail=f"Student with roll number {data.roll_number} already exists."
            )

        student = Student(

            roll_number=data.roll_number,

            name=data.name,

            father_name=data.father_name,

            parents_phone=data.parents_phone,

            email=data.email,

            gender=data.gender,

            phone=data.phone,

            dob=data.dob,

            address=data.address,

            batch_time=data.batch_time,

            joining_date=data.joining_date,

            total_fees=data.total_fees,

            student_status=data.student_status,

            course=data.course,
        )

        db.add(student)

        db.flush()

        # total_paid = 0

        for payment in data.payments:

            fee = FeePayment(

                roll_number=student.roll_number,

                amount=payment.amount,

                payment_date=payment.payment_date,

                payment_method=payment.payment_method,

                remarks=payment.remarks,

                received_by=payment.received_by,
            )

            # total_paid += payment.amount

            db.add(fee)

        # student.paid_fees = total_paid
    # 
        # student.pending_fees = student.total_fees - total_paid

        db.commit()

        student = (
            db.query(Student)
            .options(selectinload(Student.payments))
            .filter(Student.roll_number == data.roll_number)
            .first()
        )

        return student
    finally:
        db.close()


@router.get(
    "/students",
    response_model=list[StudentResponse],
)
def get_students():

    db = SessionLocal()

    try:
        students = (
            db.query(Student)
            .options(selectinload(Student.payments))
            .all()
        )


        return students
    finally:
        db.close()





@router.put(
    "/students/{roll_number}",
    response_model=StudentResponse,
)
def update_student(
    roll_number: str,
    data: StudentCreate,
):
    db = SessionLocal()

    try:
        student = (
            db.query(Student)
            .filter(Student.roll_number == roll_number)
            .first()
        )

        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found",
            )

        # Update student fields
        student.name = data.name
        student.father_name = data.father_name
        student.parents_phone = data.parents_phone
        student.email = data.email
        student.gender = data.gender
        student.phone = data.phone
        student.dob = data.dob
        student.address = data.address
        student.batch_time = data.batch_time
        student.joining_date = data.joining_date
        student.total_fees = data.total_fees
        student.student_status = data.student_status
        student.course = data.course

        db.commit()
        db.refresh(student)

        student = (
            db.query(Student)
            .options(selectinload(Student.payments))
            .filter(Student.roll_number == roll_number)
            .first()
        )

        return student

    finally:
        db.close()


