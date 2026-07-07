from fastapi import APIRouter
from app.services.settlement_engine import predict_settlement

router = APIRouter()

@router.get("/settlement-predictor")
def settlement_predictor(
    debt_amount: float,
    monthly_income: float,
    overdue_months: int
):
    return predict_settlement(
        debt_amount,
        monthly_income,
        overdue_months
    )