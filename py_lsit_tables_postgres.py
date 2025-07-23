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
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def list_all_tables(conn):
    try:
        with conn.cursor() as cur:
            query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                  AND table_type = 'BASE TABLE';
            """
            cur.execute(query)

            tables = cur.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(f"- {table[0]}")

    except Exception as e:
        print(f"Error fetching tables: {e}")

def main():
    conn = connect_to_db()
    if not conn:
        return

    list_all_tables(conn)
    conn.close()

if __name__ == "__main__":
    main()