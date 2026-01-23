from flask import Flask, request
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    name = "Slavik"
    project = "net4255-kubernetes-Slavik-c4"
    version = "V3"
    hostname = socket.gethostname()
    current_date = datetime.now()

    return f"""
    <p><b>Name:</b> {name}</p>
    
    <p><b>Project:</b> {project}</p>
    <p><b>Version:</b> {version}</p>
    <p><b>Server Hostname:</b> {hostname}</p>
    <p><b>Current Date:</b> {current_date}</p>

    <h3>Last 10 visits:</h3>
    <ul>
        <li>No db</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)