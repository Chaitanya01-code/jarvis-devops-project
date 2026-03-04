from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>JARVIS DevOps Project</h1>
    <p>Running on Host: {socket.gethostname()}</p>
    <p>Status: ACTIVE</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

