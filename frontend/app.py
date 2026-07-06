import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Powered Debt Relief & Financial Recovery Platform",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color: #0E76A8;
    text-align: center;
}

h2 {
    color: #1F4E79;
}

div.stButton > button {
    width: 100%;
    background-color: #0E76A8;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size:16px;
}

div[data-testid="metric-container"]{
    border:1px solid #e6e6e6;
    padding:15px;
    border-radius:10px;
    background:#f8f9fa;
}

</style>
""", unsafe_allow_html=True)

st.title("💰 AI Powered Debt Relief & Financial Recovery Platform")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Financial Health",
        "Settlement Predictor",
        "AI Negotiation Strategy"
    ]
)

# ---------------------------------------------------
# Financial Health
# ---------------------------------------------------

if menu == "Financial Health":

    st.header("📊 Financial Health Calculator")

    income = st.number_input(
        "Monthly Income",
        value=50000.0
    )

    expenses = st.number_input(
        "Monthly Expenses",
        value=25000.0
    )

    emi = st.number_input(
        "Total EMI",
        value=10000.0
    )

    if st.button("Calculate Financial Health"):

        try:

            response = requests.get(
                f"{API_URL}/financial-health",
                params={
                    "monthly_income": income,
                    "monthly_expenses": expenses,
                    "total_emi": emi
                }
            )

            data = response.json()

            st.success("Financial Health Analysis Completed")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Savings",
                    data.get("savings", 0)
                )

            with col2:
                st.metric(
                    "EMI Ratio",
                    f"{data.get('emi_ratio',0)}%"
                )

            st.subheader("Complete Response")
            st.json(data)

        except Exception as e:
            st.error(e)

# ---------------------------------------------------
# Settlement Predictor
# ---------------------------------------------------

elif menu == "Settlement Predictor":

    st.header("💰 Settlement Predictor")

    debt = st.number_input(
        "Debt Amount",
        value=300000.0
    )

    income = st.number_input(
        "Monthly Income",
        value=50000.0,
        key="income2"
    )

    overdue = st.number_input(
        "Overdue Months",
        value=8
    )

    if st.button("Predict Settlement"):

        try:

            response = requests.get(
                f"{API_URL}/settlement-predictor",
                params={
                    "debt_amount": debt,
                    "monthly_income": income,
                    "overdue_months": overdue
                }
            )

            data = response.json()

            st.success("Settlement Prediction Completed")

            st.metric(
                "Settlement %",
                f"{data.get('settlement_percentage',0)}%"
            )

            st.metric(
                "Risk Level",
                data.get("risk_level","N/A")
            )

            st.json(data)

        except Exception as e:
            st.error(e)

# ---------------------------------------------------
# AI Negotiation Strategy
# ---------------------------------------------------

elif menu == "AI Negotiation Strategy":

    st.header("🤖 AI Negotiation Strategy")

    loan_name = st.text_input(
        "Loan Name",
        "Personal Loan"
    )

    balance = st.number_input(
        "Outstanding Balance",
        value=250000.0
    )

    settlement = st.number_input(
        "Settlement Percentage",
        value=65.0
    )

    if st.button("Generate Strategy"):

        try:

            response = requests.get(
                f"{API_URL}/ai-negotiation-strategy",
                params={
                    "loan_name": loan_name,
                    "outstanding_balance": balance,
                    "settlement_percentage": settlement
                }
            )

            data = response.json()

            st.success("AI Strategy Generated Successfully")

            st.write("### Recommended Strategy")

            st.info(data.get("strategy", "No strategy generated"))

            st.json(data)

        except Exception as e:
            st.error(e)