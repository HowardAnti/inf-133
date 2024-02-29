from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingenieria de Sistemas"
    },
    {
        "id": 4,
        "nombre": "Howard",
        "apellido": "Anti",
        "carrera": "Fisica"
    }
]

carreras=[]

def carreras_array():
    for estudiante in estudiantes:
        sw = True
        nombre_carrera = estudiante["carrera"]
        if len(carreras)>0:
            for carrera in carreras:
                if carrera["nombre"]==nombre_carrera: sw = False
            if sw: carreras.append({"id": len(carreras), "nombre": nombre_carrera})
        else:
            carreras.append({"id": len(carreras), "nombre": nombre_carrera})

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        carreras_array()
        
        if self.path == '/estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
            
        elif self.path.startswith('/nombre/'):
            inicial = str(self.path.split("/")[-1])
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            estudiantes_seleccionados=[]
            for estudiante in estudiantes:
                nombre=estudiante["nombre"]
                if nombre.startswith(inicial):
                    estudiantes_seleccionados.append(estudiante)

            self.wfile.write(json.dumps(estudiantes_seleccionados).encode('utf-8'))

        elif self.path == '/numero_total':
            count = len(estudiantes)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(count).encode('utf-8'))
        
        elif self.path == '/carreras':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(carreras).encode('utf-8'))
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
    
    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
        
        


def run_server(port = 8000):
    try:
        server_address = ('',port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()


if __name__=='__main__':
    run_server()