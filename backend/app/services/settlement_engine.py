def predict_settlement(debt_amount, monthly_income, overdue_months):
    debt_to_income_ratio = debt_amount / monthly_income

    settlement_percentage = 50

    if overdue_months >= 6:
        settlement_percentage += 10

    if debt_to_income_ratio > 2:
        settlement_percentage += 10

    if settlement_percentage > 75:
        settlement_percentage = 75

    if settlement_percentage >= 70:
        risk_category = "High"
    elif settlement_percentage >= 60:
        risk_category = "Medium"
    else:
        risk_category = "Low"

    return {
        "debt_amount": debt_amount,
        "monthly_income": monthly_income,
        "overdue_months": overdue_months,
        "debt_to_income_ratio": round(debt_to_income_ratio, 2),
        "settlement_percentage": settlement_percentage,
        "risk_category": risk_category
    }