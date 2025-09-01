from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "DB_NAME")
DB_USER = os.getenv("DB_USER", "DB_USER")
DB_PASS = os.getenv("DB_PASS", "DB_PASS")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", users=users)

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["name"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return ("<p>User added! <a href='/'>Go back</a></p>")

if __name__ == "__main__":
    # Listen on all interfaces so Docker can route traffic
    app.run(host="0.0.0.0", port=8080)
