import requests


url = "http://localhost:8000/"

ruta_get = url + "estudiantes?nombre=Pedrito&&apellido=Garcia&&carrera=Ingenieria de Sistemas"
get_response = requests.request(
    method="GET", 
    url=ruta_get
    )
print(get_response.text)
