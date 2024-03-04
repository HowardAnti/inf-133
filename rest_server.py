from http.server import HTTPServer, BaseHTTPRequestHandler
import json


from urllib.parse import urlparse, parse_qs

class RESTRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status_code,data):
        self.send_response(status_code)
        self.send_header("Content-type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    def read_data(self):
        length_data=int(self.headers(["Content-Length"]))
        data = self.rfile.read(length_data)
        data = json.loads(data.decode("utf-8"))
        return data

    def find_student(self, id):
        return next((estudiante for estudiante in estudiantes if estudiante["id"]==id), None)

    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.response_handler(200, estudiantes)
        

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingenieria de Sistemas",
    }
]


#Get:Solicitar recurso
#Post:Crear

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