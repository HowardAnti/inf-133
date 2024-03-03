import requests

url = "http://localhost:8000/"

url_get = url + 'carrera/Economía'
url_post = url + 'estudiantes'

nuevo_estudiante_1={
    'nombre': 'Rodrigo',
    'apellido': 'Paton',
    'carrera' : 'Economía'
}

nuevo_estudiante_2={
    'nombre': 'Alexander',
    'apellido': 'Arias',
    'carrera' : 'Economía'
}

response = requests.request(
    method = 'GET',
    url = url_get
)

print(response.text)

response = requests.request(
    method = 'POST',
    url = url_post,
    json=nuevo_estudiante_1
)

print(response.text)

response = requests.request(
    method = 'POST',
    url = url_post,
    json=nuevo_estudiante_2
)

print(response.text)