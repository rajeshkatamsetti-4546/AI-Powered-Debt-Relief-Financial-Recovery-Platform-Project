from sqlalchemy import Column, Integer, Float, String
from app.database import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    loan_name = Column(String, nullable=False)
    loan_type = Column(String)
    principal_amount = Column(Float)
    interest_rate = Column(Float)
    tenure = Column(Integer)
    monthly_emi = Column(Float)
    outstanding_balance = Column(Float)