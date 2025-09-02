import psycopg
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    with psycopg.connect(dbname="postgres", user="hosting-db", host="localhost") as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS test (
                    id serial PRIMARY KEY,
                    data text)
                """)
            cur.execute("INSERT INTO test (data) VALUES (%s)", ("Hello, World!",))
            conn.commit()

            cur.execute("SELECT * FROM test")
            _, data = cur.fetchone()
            return f"<p>{data.decode('UTF-8')}</p>"
