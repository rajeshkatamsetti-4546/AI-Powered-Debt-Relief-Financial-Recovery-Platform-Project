def calculate_financial_health(monthly_income, monthly_expenses, total_emi):
    savings = monthly_income - monthly_expenses - total_emi

    if monthly_income > 0:
        emi_ratio = (total_emi / monthly_income) * 100
    else:
        emi_ratio = 0

    if emi_ratio < 30:
        stress_level = "Low"
    elif emi_ratio < 50:
        stress_level = "Medium"
    else:
        stress_level = "High"

    return {
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "total_emi": total_emi,
        "monthly_savings": savings,
        "emi_ratio": round(emi_ratio, 2),
        "stress_level": stress_level
    }