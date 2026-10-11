from sqlalchemy import create_engine, Column, String, Float, Integer, Table, MetaData
from app.config import settings
from app.storage.base import Storage

engine = create_engine(settings.DATABASE_URL)
metadata = MetaData()

# Define tables (simplified)
loans = Table("loans", metadata,
    Column("id", String, primary_key=True),
    Column("amount", Float),
    Column("borrower", String),
    Column("interest_rate", Float),
    Column("duration_months", Integer)
)

metadata.create_all(engine)

class SQLStorage(Storage):
    def get_loans(self):
        with engine.connect() as conn:
            return [dict(row) for row in conn.execute(loans.select())]

    def save_loan(self, loan):
        with engine.connect() as conn:
            conn.execute(loans.insert().values(**loan.dict()))
