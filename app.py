# hard-2-race-condition/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

stock = 1

@app.route("/health")
def health():
    return "ok"

@app.route("/buy", methods=["POST"])
def buy():
    global stock

    # BUG: no locking / atomic check
    if stock > 0:
        stock -= 1
        if stock < 0:
            return jsonify({"flag":FLAG})
        return jsonify({"status":"bought"})

    return jsonify({"error":"sold out"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
