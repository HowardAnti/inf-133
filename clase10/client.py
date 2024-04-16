import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}


new_chocolate_data = {
    "tipo_chocolate": "tableta",
    "peso": 32,
    "sabor": "coco"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "tipo_chocolate": "bombon",
    "peso": 32,
    "sabor": "naranja",
    "relleno": "frambuesa"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "tipo_chocolate": "trufa",
    "peso": 12,
    "sabor": "manzana",
    "relleno": "cacao"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())



response = requests.get(url=url)
print(response.json())


chocolate_id_to_update = 2
updated_chocolate_data = {
    "peso": 43,
    "sabor": "naranja",
    "relleno": "almendra"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET 
response = requests.get(url=url)
print(response.json())

# DELETE 
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET 
response = requests.get(url=url)
print(response.json())