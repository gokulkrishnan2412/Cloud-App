from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def get_loans(self): pass
    @abstractmethod
    def save_loan(self, loan): pass
    @abstractmethod
    def get_lendings(self): pass
    @abstractmethod
    def save_lending(self, lending): pass
    @abstractmethod
    def get_chits(self): pass
    @abstractmethod
    def save_chit(self, chit): pass

def get_storage(backend: str):
    if backend == "json":
        from app.storage.json_store import JSONStorage
        return JSONStorage()
    elif backend == "sql":
        from app.storage.sql_store import SQLStorage
        return SQLStorage()
    elif backend == "sheets":
        from app.storage.sheets_store import SheetsStorage
        return SheetsStorage()
    else:
        raise ValueError(f"Unknown backend: {backend}")
