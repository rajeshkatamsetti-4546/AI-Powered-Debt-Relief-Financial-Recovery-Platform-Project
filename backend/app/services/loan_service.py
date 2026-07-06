from sqlalchemy.orm import Session
from app.models.loan import Loan


def create_loan(db: Session, loan):
    new_loan = Loan(
        loan_name=loan.loan_name,
        loan_type=loan.loan_type,
        principal_amount=loan.principal_amount,
        interest_rate=loan.interest_rate,
        tenure=loan.tenure,
        monthly_emi=loan.monthly_emi,
        outstanding_balance=loan.outstanding_balance
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return new_loan


def get_all_loans(db: Session):
    return db.query(Loan).all()


def get_loan_by_id(db: Session, loan_id: int):
    return db.query(Loan).filter(Loan.id == loan_id).first()


def update_loan(db: Session, loan_id: int, loan_data):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()

    if loan:
        loan.loan_name = loan_data.loan_name
        loan.loan_type = loan_data.loan_type
        loan.principal_amount = loan_data.principal_amount
        loan.interest_rate = loan_data.interest_rate
        loan.tenure = loan_data.tenure
        loan.monthly_emi = loan_data.monthly_emi
        loan.outstanding_balance = loan_data.outstanding_balance

        db.commit()
        db.refresh(loan)

    return loan


def delete_loan(db: Session, loan_id: int):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()

    if loan:
        db.delete(loan)