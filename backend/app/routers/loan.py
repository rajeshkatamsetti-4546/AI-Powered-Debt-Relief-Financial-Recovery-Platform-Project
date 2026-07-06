from fastapi import APIRouter
from app.schemas.loan import LoanCreate

router = APIRouter()

@router.post("/add-loan")
def add_loan(loan: LoanCreate):
    return {
        "message": "Loan added successfully",
        "loan": loan
    }

@router.get("/loans")
def get_loans():
    return {
        "message": "Loan list",
        "data": []
    }