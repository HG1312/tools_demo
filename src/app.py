"""Orders worker: small Flask service. Uses parameterized queries (safe)."""
import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(os.environ["DATABASE_URL"])


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json(force=True)
    customer_id = data.get("customer_id")
    amount = data.get("amount")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (customer_id, amount) VALUES (%s, %s) RETURNING id",
        (customer_id, amount),
    )
    order_id = cur.fetchone()[0]
    conn.commit()
    return jsonify({"id": order_id}), 201


@app.route("/health")
def health():
    return {"status": "ok"}
