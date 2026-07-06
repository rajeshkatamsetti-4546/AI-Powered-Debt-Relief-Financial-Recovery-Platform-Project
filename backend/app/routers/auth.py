from fastapi import APIRouter
from app.schemas.auth import RegisterRequest, LoginRequest

router = APIRouter()


@router.post("/register")
def register(user: RegisterRequest):
    return {
        "message": "User registered successfully",
        "user": user
    }


@router.post("/login")
def login(user: LoginRequest):
    return {
        "message": "Login successful",
        "email": user.email
    }