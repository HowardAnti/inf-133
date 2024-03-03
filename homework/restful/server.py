from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import unquote

estudiantes = [
    {
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
        "id": 1,
    },
    {
        "nombre": "Howard",
        "apellido": "Anti",
        "carrera": "Física",
        "id": 2,
    },
    {
        "nombre": "Edward",
        "apellido": "Ruiz",
        "carrera": "Economía",
        "id": 3,
    },
]

carreras = []

def encontrar_carreras():
    for estudiante in estudiantes:
        nombre_carrera = estudiante['carrera']
        if len(carreras)>0:
            sw = True
            for carrera in carreras:
                if carrera['nombre']==nombre_carrera:
                    sw = False
            if sw: carreras.append({'id': len(carreras), 'nombre': nombre_carrera})   
        else:
            carreras.append({'id': len(carreras), 'nombre': nombre_carrera })


def encontrar_estudiantes_carrera(carrera, estudiantes_carrera):
    for estudiante in estudiantes:
        nombre_carrera = estudiante['carrera']
        if nombre_carrera == carrera:
            estudiantes_carrera.append(estudiante)


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/estudiantes":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        
        elif self.path == "/carreras":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            encontrar_carreras()
            self.wfile.write(json.dumps(carreras).encode('utf-8'))
        
        elif self.path.startswith('/carrera/'):
            send_estudiantes = []
            carrera = unquote(self.path.split("/")[-1])
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            encontrar_estudiantes_carrera(carrera, send_estudiantes) 
            self.wfile.write(json.dumps(send_estudiantes).encode('utf-8'))
            
            
        
           
        else :
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'Error': 'Ruta no existente'}).encode('utf-8'))

    def do_POST(self):
        if self.path == "/estudiantes":
            content_length = int(self.headers['Content-Length'])
            postdata = self.rfile.read(content_length)
            postdata = json.loads(postdata.decode('utf-8'))
            postdata["id"] = len(estudiantes) + 1
            estudiantes.append(postdata)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else :
            self.send_response(404)
            self.send_header('Conten-types', ' application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'Error': ' Ruta no existente'}).encode('utf-8'))
    
    def do_PUT(self):
        if self.path.startswith('/estudiantes'):
            content_length = int(self.headers['Content-Lenght'])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode('utf-8'))
            id = data['id']
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante['id'] == id), None,
            )    
            if estudiante:
                estudiante.update(data)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else : 
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'Error': 'Ruta no existente'}).encode('utf-8'))

    def do_DELETE(self):
        if self.path == '/estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
            

def run_server(port = 8000):
    try:
        server_address = ('',port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost{port}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close() 
        

if __name__ == '__main__':
    run_server()