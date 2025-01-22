 # Get the label selector used by the deployment
        label_selector = deployment.spec.selector.match_labels
        if not label_selector:
            print("No label selector found in deployment.")
            return None

        # Convert label_selector dictionary to a label query string for list_namespaced_pod
        label_query = ",".join([f"{key}={value}" for key, value in label_selector.items()])
