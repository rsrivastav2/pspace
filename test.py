from kubernetes import client, config
from datetime import datetime

# Load the Kubernetes configuration (from kubeconfig or in-cluster)
config.load_kube_config()  # Use config.load_incluster_config() if running inside a cluster

def get_pods_info(namespace=None, deployment_name=None):
    v1 = client.CoreV1Api()
    apps_v1 = client.AppsV1Api()
    
    # Get all pods in the given namespace
    pods = v1.list_namespaced_pod(namespace).items
    
    pod_details = []
    
    for pod in pods:
        # Get pod metadata
        pod_name = pod.metadata.name
        pod_status = pod.status.phase
        created_at = pod.metadata.creation_timestamp
        
        # Convert to readable datetime
        created_at_str = created_at.strftime('%Y-%m-%d %H:%M:%S') if created_at else "N/A"

        # Check if the pod belongs to the given deployment
        if deployment_name:
            owner_references = pod.metadata.owner_references or []
            for owner in owner_references:
                if owner.kind == "ReplicaSet":
                    # Fetch ReplicaSet details to check its owner (Deployment)
                    rs = apps_v1.read_namespaced_replica_set(owner.name, namespace)
                    if rs.metadata.owner_references and rs.metadata.owner_references[0].kind == "Deployment":
                        if rs.metadata.owner_references[0].name == deployment_name:
                            pod_details.append((pod_name, pod_status, created_at_str))
        else:
            pod_details.append((pod_name, pod_status, created_at_str))

    return pod_details

# Example usage:
namespace = "default"
deployment_name = "my-deployment"  # Set to None if you want all pods in the namespace

pods_info = get_pods_info(namespace, deployment_name)
for name, status, created in pods_info:
    print(f"Pod: {name}, Status: {status}, Created: {created}")
