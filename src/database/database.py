import sqlite3
from pathlib import Path

class Database:
    def __init__(self, db_location: str, migrations_path: str, db_name: str):
        print("Initializing database manager.")
        self.db_path = Path(db_location, db_name)
        self.db_location = Path(db_location)
        self.migrations_path = Path(migrations_path)
        self._conn = None

    def __enter__(self):
        print(f"Checking DB path for {self.db_path}")
        db_location_missing = not self.db_location.exists()

        if db_location_missing:
            print(f"Creating directory: {self.db_location}")
            self.db_location.mkdir(parents=True, exist_ok=True)

        self._conn = sqlite3.connect(self.db_path)
        self._ensure_configuration()
        self._apply_migrations()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Beginning __exit__")
        if self._conn is None:
            raise RuntimeError("self.conn undefined, exiting.")
        
        if exc_type is None:
            print("Committing changes.")
            self.commit()
        else:
            print("Beginning rollback.")
            self._conn.rollback()
        print(f"Closing DB connection for object {self}: {self.db_path}")
        self.close()

    def _ensure_configuration(self):
        print("Creating configuration table.")

        self._conn.execute(
            """
                CREATE TABLE IF NOT EXISTS configuration(
                    id INTEGER PRIMARY KEY CHECK(id=1),
                    schema_version INTEGER NOT NULL DEFAULT 0
                )
            """
        )

        schema_version = self._get_schema_version()
        print(f"Schema version: {schema_version}")

        if not schema_version and schema_version != 0:
            print("Inserting initial schema value.")
            self._execute(
                """INSERT INTO CONFIGURATION (id, schema_version) VALUES (1, 0)"""
            )

    def _apply_migrations(self):
        migrations = {}
        migrations_folder = self.migrations_path.iterdir()

        if not migrations_folder:
            raise RuntimeError("Migrations folder not found.")

        cur_schema_version = self._get_schema_version()

        sql_files = [file for file in migrations_folder if file.suffix == ".sql"]

        for file in sql_files:
            file_name_split = file.name.split("_")
            migration_num = int(file_name_split[0])

            with open(file, "r") as sql:
                content = sql.read()
                migrations[migration_num] = content

    def _get_schema_version(self):
        cursor = self._conn.cursor()
        cursor.execute(
            """SELECT schema_version
               FROM configuration"""
        )

        schema_version = cursor.fetchone()

        if schema_version is None:
            return None
        return schema_version[0]

    def _execute(self, sql: str, params: tuple = ()) -> sqlite3.Cursor:
        cursor = self._conn.cursor()
        cursor.execute(sql, params)

        return cursor

    def commit(self):
        self._conn.commit()

    def close(self):
        self._conn.close()