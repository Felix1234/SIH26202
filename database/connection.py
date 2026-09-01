import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "sih26202",
    "user": "postgres",
    "password": "462007"
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)