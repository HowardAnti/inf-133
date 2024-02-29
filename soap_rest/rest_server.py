from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingeniria de Siastemas",
    },
    {
        "id": 2,
        "nombre": "Edward",
        "apellido": "Ruiz",
        "carrera": "Fisica",
    },
    {
        "id": 3,
        "nombre": "Howard",
        "apellido": "Anti",
        "carrera": "Fisica",
    },
    {
        "id": 4,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingeniria de Siastemas",
    },
    {
        "id": 5,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Gastronomia",
    }
]

carreras=[]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "estudiantes":
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path =="/carreras":
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            for estudiante in estudiantes:
                sw = True
                nombre = estudiante["carrera"]
                for carrera in carreras:
                    if carrera==nombre: sw = False
                if sw: carreras.append(nombre)
            self.wfile.write(json.dumps(carreras).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error":"page not found"}).encode("utf-8"))


def run_server(port=8000):
    try:
        server_address=("",port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print("Iniciando servidor")
        httpd.serve_forever()
    
    except KeyboardInterrupt:
        print("Apagamdopservidor")
        httpd.socket.accept




if __name__=="__main__":
    run_server()