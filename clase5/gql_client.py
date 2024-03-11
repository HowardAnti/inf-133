import requests
url = 'http://localhost:8000/graphql'
# Definir la consulta GraphQL
'''query1 = """
    {
        estudiantes {

            nombre
            
        }
        
    }
"""

# Definir la URL del servidor GraphQL


# Solicitud POST al servidor GraphQL
response1 = requests.post(url, json={'query': query1})
print(response1.text)

query2 = """
    {
        estudiantes {
            nombre
            apellido
        }
    }
"""

response2 = requests.post(url, json={'query': query2})
print(response2.text)

query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response3 = requests.post(url, json={'query': query})
print(response3.text)

query = """
    {
        estudiantePorNombreApellido(nombre: "Jose", apellido: "Lopez"){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response3 = requests.post(url, json={'query': query})
print(response3.text)

query = """
    {
        estudiantePorCarrera(carrera: "Fisica"){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response3 = requests.post(url, json={'query': query})
print(response3.text)'''

query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)
query_crear = """
mutation {
        crearEstudiante(nombre: "Oscar", apellido: "Gomez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)
query_crear = """
mutation {
        crearEstudiante(nombre: "Angelo", apellido: "Gomez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)
query_crear = """
mutation {
        crearEstudiante(nombre: "Leo", apellido: "Gomez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

query = """
    {
        estudiantePorCarrera(carrera: "Arquitectura"){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response3 = requests.post(url, json={'query': query})
print(response3.text)

query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

query = """
    {
        estudiantes {

            nombre
            carrera
            
        }
        
    }
"""

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query})
print(response.text)


query_actualizar = """
mutation {
        updateEstudiante(nombre: "Jose", apellido: "Lopez", carrera: "Antropologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_actualizar})
print(response_mutation.text)


query = """
    {
        estudiantes {

            nombre
            carrera
            
        }
        
    }
"""

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query})

print(response.text)