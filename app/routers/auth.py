from fastapi import APIRouter,HTTPException,Depends
from ..database import SessionLocal
from ..models.user import User
from ..schemas.loginrequest import LoginRequest
from ..core.security import verify_password
from ..core.security import create_access_token
from ..core.security import hash_password
from ..core.security import get_current_user

router=APIRouter()

@router.get("/verify-token")
def verify_token(current_user=Depends(get_current_user)):
    return {
        "valid": True,
        "username": current_user.username,
        "role": current_user.role,
    }

@router.post("/login")

def login(data:LoginRequest):

    db=SessionLocal()

    user=db.query(User).filter(
        User.username==data.username
    ).first()

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Username"
        )

    if not verify_password(data.password,user.password):
        raise HTTPException(
            status_code=401,
            detail="Wrong Password"
        )

    token=create_access_token(
        user.username
    )

    return{

        "token":token,

        "username":user.username,

        "role":user.role

    }

@router.post("/register")

def register(data:LoginRequest):

    db=SessionLocal()

    new_user=User(

        username=data.username,

        password=hash_password(
            data.password
        ),

        role="Admin"

    )

    db.add(new_user)

    db.commit()

    return{

        "message":"User Created"

    }




















