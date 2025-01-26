from flask import Flask, jsonify, request
from kubernetes import client, config

app = Flask(__name__)

# Load kubeconfig to authenticate with the AKS cluster
config.load_kube_config()  # Assumes kubeconfig is set up to access AKS

@app.route('/get-deployments', methods=['GET'])
def get_deployments():
    # Create a Kubernetes API client
    v1_apps = client.AppsV1Api()

    # List deployments from all namespaces
    deployments = v1_apps.list_deployment_for_all_namespaces()

    # Extract deployment names from the response
    deployment_names = [deployment.metadata.name for deployment in deployments.items]

    return jsonify(deployment_names)

@app.route('/get-deployment-details', methods=['GET'])
def get_deployment_details():
    # Get the deployment name from the request
    deployment_name = request.args.get('deployment_name')

    # Simulate different second dropdown options based on the selected deployment
    if deployment_name == "deployment1":
        second_dropdown_options = ["Detail A", "Detail B", "Detail C"]
    elif deployment_name == "deployment2":
        second_dropdown_options = ["Detail D", "Detail E", "Detail F"]
    else:
        second_dropdown_options = []

    return jsonify(second_dropdown_options)

if __name__ == '__main__':
    app.run(debug=True)
