from pydantic import BaseModel

class LoanCreate(BaseModel):
    loan_name: str
    loan_type: str
    principal_amount: float
    interest_rate: float
    tenure: int
    monthly_emi: float
    outstanding_balance: float