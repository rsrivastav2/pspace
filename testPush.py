rom kubernetes import client, config

def main():
    # Load kubeconfig from default location (~/.kube/config)
    config.load_kube_config()

    # Create a Kubernetes API client
    api_instance = client.CoreV1Api()

    # List all pods in the default namespace
    print("Listing pods with their IPs:")
    ret = api_instance.list_namespaced_pod(namespace='default')
    for pod in ret.items:
        print(f"{pod.metadata.name} {pod.status.pod_ip}")

if __name__ == "__main__":
    main()
