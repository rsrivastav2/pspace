# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import paramiko
import threading
import uuid

app = Flask(__name__)
CORS(app)

jobs = {}  # In-memory job status tracker

@app.route("/run-job", methods=["POST"])
def run_job():
    data = request.json
    job_id = str(uuid.uuid4())
    script_path = data.get("script_path")
    host = data.get("host")
    username = data.get("username")
    key_path = data.get("key_path")

    jobs[job_id] = "Queued"

    def ssh_job():
        try:
            jobs[job_id] = "Running"
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, username=username, key_filename=key_path)
            stdin, stdout, stderr = ssh.exec_command(f"bash {script_path}")
            exit_status = stdout.channel.recv_exit_status()
            ssh.close()
            if exit_status == 0:
                jobs[job_id] = "Success"
            else:
                jobs[job_id] = f"Failed (exit {exit_status})"
        except Exception as e:
            jobs[job_id] = f"Error: {str(e)}"

    threading.Thread(target=ssh_job).start()

    return jsonify({"job_id": job_id})

@app.route("/job-status/<job_id>", methods=["GET"])
def job_status(job_id):
    return jsonify({"status": jobs.get(job_id, "Not Found")})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
