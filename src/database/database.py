import sqlite3
from pathlib import Path

class Database:
    def __init__(self, db_location, db_name):
        print("Initializing database manager.")
        self.db_path = Path(db_location, db_name)
        self.db_location = Path(db_location)
        self.conn = None
        self.cursor = None

    def __enter__(self):
        print(f"Checking DB path for {self.db_path}")
        db_location_missing = not self.db_location.exists()

        if db_location_missing:
            print(f"Creating directory: {self.db_location}")
            self.db_location.mkdir(parents=True, exist_ok=True)

        self.conn = sqlite3.connect(self.db_path)
        self._ensure_configuration()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Beginning __exit__")
        if self.conn is None:
            raise RuntimeError("self.conn undefined, exiting.")
        
        if exc_type is None:
            print("Committing changes.")
            self.conn.commit()
        else:
            print("Beginning rollback.")
            self.conn.rollback()
        print(f"Closing DB connection for object {self}: {self.db_path}")
        self.conn.close()

    def _ensure_configuration(self):
        print("Creating configuration table.")

        self.conn.execute(
            """
                CREATE TABLE IF NOT EXISTS configuration(
                    id INTEGER PRIMARY KEY CHECK(id=1),
                    schema_version INTEGER NOT NULL DEFAULT 0
                )
            """
        )

        # Next step, extract this out to a helper function and start on the migration functions
        row = self.conn.execute(
            """SELECT schema_version FROM configuration"""
        ).fetchone()

        if not row:
            print("Inserting initial schema value.")
            self.conn.execute(
                """INSERT INTO CONFIGURATION (id, schema_version) VALUES (1, 0)"""
            )

