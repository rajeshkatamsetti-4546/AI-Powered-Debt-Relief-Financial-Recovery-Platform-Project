from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.loan import LoanCreate
from app.services.loan_service import (
    create_loan,
    get_all_loans,
    get_loan_by_id,
    update_loan,
    delete_loan
)

router = APIRouter()


@router.post("/add-loan")
def add_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    new_loan = create_loan(db, loan)
    return {
        "message": "Loan added successfully",
        "loan_id": new_loan.id
    }


@router.get("/loans")
def get_loans(db: Session = Depends(get_db)):
    return get_all_loans(db)


@router.get("/loan/{loan_id}")
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = get_loan_by_id(db, loan_id)

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    return loan


@router.put("/loan/{loan_id}")
def edit_loan(
    loan_id: int,
    loan: LoanCreate,
    db: Session = Depends(get_db)
):
    updated_loan = update_loan(db, loan_id, loan)

    if updated_loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    return {
        "message": "Loan updated successfully",
        "loan": updated_loan
    }


@router.delete("/loan/{loan_id}")
def remove_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):
    deleted_loan = delete_loan(db, loan_id)

    if deleted_loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    return {
        "message": "Loan deleted successfully"
    }