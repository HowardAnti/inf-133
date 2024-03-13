import requests


url = "http://localhost:8000/"

ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

ruta_put = url + "estudiantes/2"
update_estudiante = {
    "nombre": "Howard",
    "apellido": "Ruiz",
    "carrera": "Fisica",
}
post_response = requests.request(method="PUT", url=ruta_put, json=update_estudiante)
print(post_response.text)

post_response = requests.request(method="DELETE", url=ruta_get)
print(post_response.text)


