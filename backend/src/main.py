from fastapi import FastAPI, Depends
from backend.models import Loan, Lending, Chit
from backend.storage.base import get_storage
from backend.config import settings

app = FastAPI(title="Finance App")

storage = get_storage(settings.STORAGE_BACKEND)

@app.get("/loans")
def get_loans():
    return storage.get_loans()

@app.post("/loans")
def create_loan(loan: Loan):
    storage.save_loan(loan)
    return {"status": "success"}

@app.get("/lendings")
def get_lendings():
    return storage.get_lendings()

@app.post("/lendings")
def create_lending(lending: Lending):
    storage.save_lending(lending)
    return {"status": "success"}

@app.get("/chits")
def get_chits():
    return storage.get_chits()

@app.post("/chits")
def create_chit(chit: Chit):
    storage.save_chit(chit)
    return {"status": "success"}
