from ..orbital import Celestrak
from ..database import Database

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

celestrakProvider = Celestrak()
iss_omm_test = ""

"""
try:
    iss_omm_test = celestrakProvider.retrieve_omm(norad_id=25544).dict()
except Exception as e:
    print(type(e).__name__)
    print(e)

print(iss_omm_test)
"""

if __name__ == "__main__":
    testDB = Database(DATA_DIR, "345.db")

    print(testDB.conn)