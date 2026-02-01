from flask import Flask, jsonify, request
import time
import socket

app = Flask(__name__)
START_TIME = time.time()

@app.route("/")
def home():
    return jsonify(
        service="status-service",
        hostname=socket.gethostname(),
        status="running"
    )

@app.route("/health")
def health():
    return jsonify(ok=True)

@app.route("/uptime")
def uptime():
    return jsonify(
        uptime_seconds=int(time.time() - START_TIME)
    )

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify(
        received=data,
        processed_by="vm1"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
