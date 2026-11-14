import sqlite3
from pathlib import Path

class Database():
    def __init__(self, db_location, db_name):
        self.db_location = Path(db_location)
        self.conn = None

        try:
            self.db_path = Path(db_location, db_name)
        except TypeError:
            print("Could not coerce input parameters to os.Pathlike.")

    def __enter__(self): 
        db_location_missing = not self.db_location.exists()

        if db_location_missing:
            print(f"Creating directory: {self.db_location}")
            self.db_location.mkdir(parents=True, exist_ok=True)

        self.conn = sqlite3.connect(self.db_path)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn is None:
            raise RuntimeError("self.conn undefined, exiting.")
        
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()
