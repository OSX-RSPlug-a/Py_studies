import psycopg2
from psycopg2 import sql
import ssl


DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'sslmode': 'verify-full',
    'sslrootcert': 'ssl/ca.crt'
}

def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = False
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def insert_data(cursor):
    try:
    
        cursor.execute(
            sql.SQL("INSERT INTO table1 (id, name) VALUES (%s, %s)"),
            (1, 'Alice')
        )

        cursor.execute(
            sql.SQL("INSERT INTO table2 (id, description) VALUES (%s, %s)"),
            (101, 'Project Alpha')
        )

        cursor.execute(
            sql.SQL("INSERT INTO table3 (name, value) VALUES (%s, %s)"),
            ('Setting1', 'Enabled')
        )

        print("All inserts successful.")

    except Exception as e:
        print(f"Error during inserts: {e}")
        raise

def main():
    conn = connect_to_db()
    if not conn:
        return

    try:
        with conn.cursor() as cur:
            insert_data(cur)
            conn.commit()
    except Exception as e:
        print(f"Rolling back transaction: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()