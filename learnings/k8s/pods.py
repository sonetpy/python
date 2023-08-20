from kubernetes import client

def get_node_info():
    configuration = client.Configuration()
    configuration.host = "https://192.168.116.131:6443"

    # Disable SSL certificate validation (not recommended for production)
    configuration.verify_ssl = False

    configuration.api_key = {"authorization": "Bearer sog05x.ht4uhkaxsi0za0tp"}

    api = client.CoreV1Api(client.ApiClient(configuration))

    try:
        nodes = api.list_node().items

        for node in nodes:
            print("Node Name:", node.metadata.name)
            # ... (rest of the code)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    get_node_info()
