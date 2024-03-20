from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        

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