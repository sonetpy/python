import requests
import json
import urllib
def jet(source, destination):
    #print('City Name should be in iata format like Mumbai: BOM, Delhi: DEL')
    #dep_iata=input('Departure City: ')
    #arr_iata=input('Arrival City: ')
    params = {
    'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiY2IyMDA5ODBlNTlmOTVmNTA4YzU0MzM5NDYwZTdjZjJiNjM1ODZkYWNlZDAxYzFmOTJhY2U3YmVlZmFhMmJiMTliYmVjNjc3YTQzY2Y1MzciLCJpYXQiOjE2NTMyODQyNDQsIm5iZiI6MTY1MzI4NDI0NCwiZXhwIjoxNjg0ODIwMjQ0LCJzdWIiOiI0OTg0Iiwic2NvcGVzIjpbXX0.AjQorLAsINjaeozE9XNlf6FdCqqhpQ3i5hRVZBAtG__2v1cpRXa8IMzdDXUOh0S_hUyidq2J7165Awxn82RlUQ'
    ,'flight_status': 'active'
    ,'dep_iata': source
    ,'arr_iata': destination
    }
    response = requests.get('https://app.goflightlabs.com/flights',params)
    data = response.json()
    #data = json.dumps(response.json())
    #data_loads = json.loads(data)
    #print("Entire JSON format")
    #print("\n")
    #print("Print Just 1 flight detail\n")
    #print(data[1]["flight"]["iata"])
    #print("Print all the Flights\n")
    num_of_flight = []
    for i in range(len(data)):
        num_of_flight = data[i]["flight"]["iata"]
        return (num_of_flight)