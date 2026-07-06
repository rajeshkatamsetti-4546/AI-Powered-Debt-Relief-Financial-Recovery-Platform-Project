def generate_negotiation_strategy(
    loan_name,
    outstanding_balance,
    settlement_percentage
):
    try:
        settlement_amount = outstanding_balance * (settlement_percentage / 100)

        strategy = f"""
Loan Name: {loan_name}

Recommended Settlement: {settlement_percentage}%

Settlement Amount: ₹{settlement_amount:.2f}

Negotiation Tips:
1. Explain your financial hardship honestly.
2. Request a one-time settlement.
3. Ask for waiver of penalties.
4. Ask for written confirmation before payment.
"""

        return {
            "status": "success",
            "loan_name": loan_name,
            "settlement_percentage": settlement_percentage,
            "settlement_amount": round(settlement_amount, 2),
            "strategy": strategy
        }

    except Exception:
        return {
            "status": "fallback",
            "loan_name": loan_name,
            "settlement_percentage": 50,
            "settlement_amount": outstanding_balance * 0.5,
            "strategy": (
                "Unable to generate an AI negotiation strategy at the moment. "
                "Use the default settlement recommendation of 50% and "
                "contact the lender to discuss repayment options."
            )
        }