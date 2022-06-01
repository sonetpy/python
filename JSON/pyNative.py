import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://httpbin.org/get')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

# Let’s see how to iterate all JSON key-value pairs one-by-one
print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    print(key, ":", value)


# Access JSON key directly from the response using the key name
print("Access directly using a JSON key name")
print("URL is ")
print(jsonResponse["url"])

#Access Nested JSON key directly from response
print("Access nested JSON keys")
print("Host is is ")
print(jsonResponse["headers"]["Host"])