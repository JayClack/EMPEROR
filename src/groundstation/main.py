from ..orbital import Celestrak
from ..database import Database

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

celestrakProvider = Celestrak()
iss_omm_test = ""

if __name__ == "__main__":
    with Database(DATA_DIR, "test.db") as testDB:
        print(testDB)