from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"Helloo from Kubernetes Pod: {hostname}"

app.run(host="0.0.0.0", port=5000)
