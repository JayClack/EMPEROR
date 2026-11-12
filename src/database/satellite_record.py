import sqlite3
import os

class SatelliteRecordDB():
    db_name = "SatelliteRecordDB"
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)

"""  
TODO, set up initial DB using the docus here: https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
INVESTIGATE WHETHER TO USE SQLALCHEMY OR SQLITE3
"""