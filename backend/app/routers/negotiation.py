from fastapi import APIRouter
from app.services.negotiation_engine import generate_negotiation_strategy

router = APIRouter()

@router.get("/ai-negotiation-strategy")
def ai_negotiation_strategy(
    loan_name: str,
    outstanding_balance: float,
    settlement_percentage: float
):
    return generate_negotiation_strategy(
        loan_name,
        outstanding_balance,
        settlement_percentage
    )