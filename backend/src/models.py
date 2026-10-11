from pydantic import BaseModel
from typing import List

class Loan(BaseModel):
    id: str
    amount: float
    borrower: str
    interest_rate: float
    duration_months: int

class Lending(BaseModel):
    id: str
    lender: str
    loan_id: str
    amount: float

class Chit(BaseModel):
    id: str
    members: List[str]
    total_amount: float
    duration_months: int
