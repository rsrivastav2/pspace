from flask import Flask, jsonify
from flask_cors import CORS
import paramiko

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React

# Remote Unix Server Info
hostname = "10.0.0.5"
username = "ubuntu"
password = "your_password"  # Or use SSH key instead
remote_script = "/home/ubuntu/myscript.sh"

@app.route("/run-job", methods=["POST"])
def run_shell_script():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(f"bash {remote_script}")
        output = stdout.read().decode()
        error = stderr.read().decode()

        ssh.close()
        return jsonify({
            "status": "success",
            "output": output,
            "error": error
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
