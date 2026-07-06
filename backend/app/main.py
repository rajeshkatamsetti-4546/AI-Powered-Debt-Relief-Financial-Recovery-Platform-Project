from fastapi import FastAPI
from app.database import Base, engine
from app.models import user, loan
from app.routers import auth
from app.routers import loan as loan_router
from app.routers import financial
from app.routers import settlement
from app.routers import negotiation

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Powered Debt Relief Financial Recovery Platform",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(loan_router.router)
app.include_router(financial.router)
app.include_router(settlement.router)
app.include_router(negotiation.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Powered Debt Relief Financial Recovery Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "Running Successfully"
    }
