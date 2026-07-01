from flask import Flask, render_template
from datetime import datetime
import platform
import socket

app = Flask(__name__)


@app.route("/")
def home():
    cluster = {
        "status": "Healthy",
        "environment": "Production",
        "cluster_name": "Minikube Cluster",
        "namespace": "default",
        "nodes": 1,
        "pods": 6,
        "deployments": 2,
        "services": 2,
        "image": "suchit10/github-actions-kubernetes:latest",
        "version": "v1.0.0",
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "python": platform.python_version(),
        "last_update": datetime.now().strftime("%d %B %Y | %I:%M:%S %p"),
    }

    return render_template("index.html", cluster=cluster)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)