import sqlite3
import os
from pathlib import Path

class Database():
    def __init__(self, db_location, db_name):
        self.db_location = Path(db_location)
        self.db_path = self.db_location / db_name

        try:
            self.db_path = Path(db_location, db_name)
        except TypeError:
            print("Could not coerce input parameters to os.Pathlike.")

        self.conn = self.setup_database()

    def __enter__(self): 
        self.conn = self.setup_database()

        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def _location_exists(self, path):
        print(f"Checking path: {path}")
        path_exists = os.path.exists(path)
        if path_exists:
            print(f"Path:{path} located")
            return True
        return False

    def setup_database(self):
        db_location_missing = not self._location_exists(self.db_location)

        if db_location_missing:
            print(f"Creating directory: {self.db_location}")
            os.makedirs(self.db_location)

        return sqlite3.connect(self.db_path)
            
