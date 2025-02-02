from flask import Flask, jsonify
from kubernetes import client, config

app = Flask(__name__)

# Load Kubernetes config (assumes running inside a cluster or kubeconfig is set)
config.load_kube_config()  # Use config.load_incluster_config() if running inside a cluster
v1 = client.CoreV1Api()

@app.route('/pod-status/<namespace>/<deployment>', methods=['GET'])
def get_pod_status(namespace, deployment):
    try:
        # Get all pods in the namespace
        pods = v1.list_namespaced_pod(namespace)
        
        # Filter pods belonging to the given deployment
        pod_status_list = []
        for pod in pods.items:
            if deployment in pod.metadata.name:
                pod_status_list.append({
                    "pod_name": pod.metadata.name,
                    "status": pod.status.phase
                })
        
        if not pod_status_list:
            return jsonify({"error": "No pods found for deployment"}), 404

        return jsonify(pod_status_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
