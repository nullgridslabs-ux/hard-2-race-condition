# hard-2-race-condition/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

stock = 1

@app.route("/")
def index():
    return """
<h2>Flash Sale Backend</h2>
<p>Limited stock checkout API for campaign users.</p>
<ul>
<li>POST /buy</li>
<li>GET /health</li>
</ul>
<p>Only one item available.</p>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/buy", methods=["POST"])
def buy():
    global stock

    if stock > 0:
        stock -= 1
        if stock < 0:
            return jsonify({"flag":FLAG})
        return jsonify({"status":"bought"})

    return jsonify({"error":"sold out"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)
