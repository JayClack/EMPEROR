from orbital import Celestrak
from database import Database
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

celestrakProvider = Celestrak()
iss_omm_test = ""

if __name__ == "__main__":
    with Database(DATA_DIR, "groundstationDatabase.db") as groundstationDatabase:
        # Here we query the table sqlite_master, and it returns a list of tuples, each tuple being a row
        tables_query = """
            SELECT name from sqlite_master where type='table'
        """

        cursor = groundstationDatabase.conn.cursor()
        # List of tuples
        tables = cursor.execute(tables_query).fetchall()
        print(f"Tables: {tables}, {type(tables)}")

        for table in tables:
            param = table[0]

            data = cursor.execute(f"SELECT schema_version FROM {param}").fetchall()
            print(f"schema_version row: {data[0]}")