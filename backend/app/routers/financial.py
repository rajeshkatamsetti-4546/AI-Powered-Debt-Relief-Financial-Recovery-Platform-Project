from fastapi import APIRouter
from app.services.financial_engine import calculate_financial_health

router = APIRouter()

@router.get("/financial-health")
def financial_health(
    monthly_income: float,
    monthly_expenses: float,
    total_emi: float
):
    return calculate_financial_health(
        monthly_income,
        monthly_expenses,
        total_emi
    )