from flask import Flask, request
import socket
from datetime import datetime
import os
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client.net4255
logs_collection = db.logs

@app.route("/")
def index():
    name = "Slavik"
    project = "net4255-kubernetes-Slavik-c3"
    version = "V2"
    hostname = socket.gethostname()
    current_date = datetime.now()
    client_ip = request.remote_addr

    logs_collection.insert_one({
        "ip": client_ip, 
        "date": current_date
    })

    last_logs = list(logs_collection.find().sort("date", -1).limit(10))
    
    logs_html = ""
    for log in last_logs:
        logs_html += f"<li>IP: {log['date']} | Date : {log['ip']}</li>"

    return f"""
    <p><b>Name:</b> {name}</p>
    <p><b>Project:</b> {project}</p>
    <p><b>Version:</b> {version}</p>
    <p><b>Server Hostname:</b> {hostname}</p>
    <p><b>Current Date:</b> {current_date}</p>

    <h3>Last 10 visits:</h3>
    <ul>
        {logs_html}
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)