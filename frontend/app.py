import streamlit as st

st.set_page_config(
    page_title="AI Powered Debt Relief Financial Recovery Platform",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Powered Debt Relief Financial Recovery Platform")

st.write("Welcome to the AI Powered Debt Relief Financial Recovery Platform.")

st.header("Customer Details")

name = st.text_input("Customer Name")
income = st.number_input("Monthly Income", min_value=0)
debt = st.number_input("Total Debt", min_value=0)

if st.button("Analyze"):
    st.success("Analysis completed successfully!")
    st.write(f"Customer: {name}")
    st.write(f"Monthly Income: ₹{income}")
    st.write(f"Total Debt: ₹{debt}")