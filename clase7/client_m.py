
import requests

url = "http://localhost:8000/delivery"


data = {"vehicle_type": "motorcycle"}

response = requests.post(url, headers={"Content-Type": "application/json"}, json=data)

print(response.text)

data = {"vehicle_type": "drone"}

response = requests.post(url, headers={"Content-Type": "application/json"}, json=data)

print(response.text)


data = {"vehicle_type": "scout"}

response = requests.post(url, headers={"Content-Type": "application/json"}, json=data)

print(response.text)