from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/devops_db")

def connect_db():
    """Try connecting to the database."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def home():
    return "Hello, DevOps Exam!"

@app.route("/db-test")
def db_test():
    """Test database connection"""
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database Connection Failed: {conn}", 500

    cursor = conn.cursor()
    cursor.execute("SELECT 'Database Connected Successfully!'")
    message = cursor.fetchone()[0]
    conn.close()
    return message, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
