from fastapi import FastAPI
from .routers.auth import router
from .routers.studentadd import router as student_router

app=FastAPI()
app.include_router(router)
app.include_router(student_router)