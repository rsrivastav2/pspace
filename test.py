from kubernetes import client, config
from kubernetes.client.rest import ApiException

def get_pod_status_by_deployment(deployment_name, namespace='default'):
    try:
        # Load kube config
        config.load_kube_config()

        # Initialize Kubernetes API client
        v1 = client.CoreV1Api()

        # Get the deployment to find the selector (label) used for pods
        apps_v1 = client.AppsV1Api()
        deployment = apps_v1.read_namespaced_deployment(deployment_name, namespace)

        # Extract label selector used by the deployment
        label_selector = deployment.spec.selector.match_labels

        # Get list of pods with the label selector (associated with the deployment)
        pods = v1.list_namespaced_pod(namespace, label_selector=f"app={label_selector['app']}")

        # Get the status of each pod
        pod_statuses = {}
        for pod in pods.items:
            pod_statuses[pod.metadata.name] = pod.status.phase

        return pod_statuses

    except ApiException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
deployment_name = 'my-deployment'  # Replace with your deployment name
namespace = 'default'  # Replace with your namespace
pod_statuses = get_pod_status_by_deployment(deployment_name, namespace)

if pod_statuses:
    for pod_name, status in pod_statuses.items():
        print(f"Pod: {pod_name}, Status: {status}")
