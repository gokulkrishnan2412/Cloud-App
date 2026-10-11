from app.models import Loan

def test_loan_model():
    loan = Loan(id="1", amount=1000, borrower="Alice", interest_rate=5.0, duration_months=12)
    assert loan.amount == 1000
