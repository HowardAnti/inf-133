import requests

url = "http://localhost:8000/pizza"

mi_pizza = {
    "tamaño": "Mediana",
    "masa": "Gruesa",
    "toppings": ["Champiñones", "Queso"]
}
response = requests.post(url, json=mi_pizza, headers={'Content-type': 'application/json'})
print(response.text)