import requests


url = "http://localhost:8000/"

'''
ruta_get = url + "lista_estudiantes"

get_response = requests.request(
    method="GET", 
    url=ruta_get
)



print(get_response.text)



print("---------------------------")

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
)

print(post_response.text)

'''
'''
ruta_buscar = url + "buscar_nombre"

response3 = requests.request(
    method="FIND",
    url=ruta_find
)

print(response3.text)

'''

ruta_nombre_inicial = url + "nombre/P"

response3 = requests.request(
    method="GET",
    url=ruta_nombre_inicial
)


ruta_carrera = url + "carreras"

response4 = requests.request(
    method="GET",
    url=ruta_carrera
)

ruta_contar = url + "numero_total"

response5 = requests.request(
    method="GET",
    url=ruta_contar
)


print(response4.text)