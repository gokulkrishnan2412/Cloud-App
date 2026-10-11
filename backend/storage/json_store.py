import json
from pathlib import Path
from backend.storage.base import Storage

DATA_FILE = Path("data.json")

class JSONStorage(Storage):
    def __init__(self):
        if not DATA_FILE.exists():
            DATA_FILE.write_text(json.dumps({"loans": [], "lendings": [], "chits": []}))

    def _read(self):
        return json.loads(DATA_FILE.read_text())

    def _write(self, data):
        DATA_FILE.write_text(json.dumps(data, indent=2))

    def get_loans(self):
        return self._read()["loans"]

    def save_loan(self, loan):
        data = self._read()
        data["loans"].append(loan.dict())
        self._write(data)

    def get_lendings(self):
        return self._read()["lendings"]

    def save_lending(self, lending):
        data = self._read()
        data["lendings"].append(lending.dict())
        self._write(data)

    def get_chits(self):
        return self._read()["chits"]

    def save_chit(self, chit):
        data = self._read()
        data["chits"].append(chit.dict())
        self._write(data)
