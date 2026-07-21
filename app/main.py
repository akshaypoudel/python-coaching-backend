from fastapi import FastAPI
from .routers.auth import router as auth_router
from .routers.studentadd import router as student_router
from .routers.fee_payment import router as fee_router

app=FastAPI()
app.include_router(auth_router)
app.include_router(student_router)
app.include_router(fee_router)