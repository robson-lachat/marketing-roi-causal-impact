# load_data.py

from pathlib import Path

import duckdb

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database.duckdb"
MODEL_DIR = BASE_DIR / "models"


def run_sql_file(con, file_path):
    with open(file_path, "r") as f:
        sql = f.read()
    con.execute(sql)


def initialize_db():
    # Remove existing database if it exists
    if DB_PATH.exists():
        DB_PATH.unlink()
        print("🗑️ Existing database removed.")

    # Creates the connection with the local database
    with duckdb.connect(str(DB_PATH)) as con:
        print("📥 Loading data to DuckDB...")

        # Creating tables from files in the data/ folder
        try:
            run_sql_file(con, MODEL_DIR / "create_donations.sql")
            run_sql_file(con, MODEL_DIR / "create_donors.sql")
            run_sql_file(con, MODEL_DIR / "create_campaigns.sql")

            print("✅ Data loaded successfully into DuckDB.")

            print("\n--- Summary ---")
            for table in ["donations", "donors", "campaigns"]:
                count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                print(f"📊 {table.capitalize()}: {count} records")

        except Exception as e:
            print(f"❌ Error loading data: {e}")


if __name__ == "__main__":
    initialize_db()
