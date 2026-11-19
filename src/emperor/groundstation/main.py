from emperor.orbital import Celestrak
from emperor.database import Database
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
MIGRATIONS_DIR = Path(__file__).parent / "migrations"

celestrakProvider = Celestrak()
iss_omm_test = ""

if __name__ == "__main__":
    params = {
        "db_location": DATA_DIR,
        "migrations_path": MIGRATIONS_DIR,
        "db_name": "groundstationDatabase.db"
    }

    with Database(**params) as groundstationDatabase:
        # Here we query the table sqlite_master, and it returns a list of tuples, each tuple being a row
        tables_query = """
            SELECT name from sqlite_master where type='table'
        """