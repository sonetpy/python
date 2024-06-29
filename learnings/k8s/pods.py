from kubernetes import client, config

def list_pods(namespace='default'):
    # Load the kubeconfig file
    config.load_kube_config()

    # Create a Kubernetes API client
    v1 = client.CoreV1Api()

    print(f"Listing pods in namespace {namespace}:")
    ret = v1.list_namespaced_pod(namespace)
    for pod in ret.items:
        print(f"{pod.metadata.name}\t{pod.status.phase}\t{pod.spec.node_name}")

if __name__ == "__main__":
    list_pods()