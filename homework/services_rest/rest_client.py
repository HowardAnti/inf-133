import requests


url = "http://localhost:8000/"

'''
ruta_get = url + "estudiantes"

get_response = requests.request(
    method="GET", 
    url=ruta_get
)

ruta_post = url + "agrega_estudiante"

nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}

post_response = requests.request(
    method="POST",
    url=ruta_post,
    json=nuevo_estudiante
)'''

ruta_nombre_inicial = url + "buscar_nombre/P"

response3 = requests.request(
    method="GET",
    url=ruta_nombre_inicial
)


ruta_carrera = url + "contar_carreras"

response4 = requests.request(
    method="GET",
    url=ruta_carrera
)

ruta_contar = url + "total_estudiantes"

response5 = requests.request(
    method="GET",
    url=ruta_contar
)


print(response5.text)