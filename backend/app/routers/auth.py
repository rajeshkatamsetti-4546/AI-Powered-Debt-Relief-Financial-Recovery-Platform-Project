from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.user_service import create_user

router = APIRouter()


@router.post("/register")
def register(user: RegisterRequest, db: Session = Depends(get_db)):
    new_user = create_user(
        db=db,
        full_name=user.full_name,
        email=user.email,
        password=user.password
    )

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "full_name": new_user.full_name,
        "email": new_user.email
    }


@router.post("/login")
def login(user: LoginRequest):
    return {
        "message": "Login successful",
        "email": user.email
    }