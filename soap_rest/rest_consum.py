import requests

url = "http://localhost:8000/carreras"

response = requests.request(
    method="GET",
    url=url
)

print(response.text)

#el metodo de consulta y la forma de acceder al servicio-endpoint
#soap es un protocolo xml rest es una architectura json