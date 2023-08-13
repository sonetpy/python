import kubernetes.client
from kubernetes import client, config

# Load the kubeconfig file
config.load_kube_config()

# Create an API object
v1 = kubernetes.client.CoreV1Api()

# Get all the pods
ret = v1.list_pod_for_all_namespaces(watch=False)

# Print the pod name and node name
for pod in ret.items:
    print(f"{pod.metadata.name} is running on {pod.spec.node_name}")
