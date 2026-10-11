from app.storage.base import Storage

class SheetsStorage(Storage):
    def get_loans(self):
        # TODO: Implement Google Sheets API read
        return []

    def save_loan(self, loan):
        # TODO: Implement Google Sheets API write
        pass

    def get_lendings(self): return []
    def save_lending(self, lending): pass
    def get_chits(self): return []
    def save_chit(self, chit): pass
