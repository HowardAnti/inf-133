from http.server import HTTPServer, BaseHTTPRequestHandler
import json


chocolates = {}


class Chocolate:
    def __init__(self, tipo_chocolate, peso, sabor, relleno):
        self.tipo_chocolate = tipo_chocolate
        self.peso = peso
        self.sabor = sabor
        self.relleno = relleno


class Tableta(Chocolate):
    def __init__(self, peso, sabor):
        super().__init__("tableta", peso, sabor, None)


class Bombon(Chocolate):
    def __init__(self, peso, sabor, relleno):
        super().__init__("bombon", peso, sabor, relleno)

class Trufa(Chocolate):
    def __init__(self, peso, sabor, relleno):
        super().__init__("trufa", peso, sabor, relleno)

class Chocolateria:
    @staticmethod
    def create_chocolate(tipo_chocolate, peso, sabor, relleno):
        if tipo_chocolate == "tableta":
            return Tableta(peso, sabor)
        elif tipo_chocolate == "bombon":
            return Bombon(peso, sabor, relleno)
        elif tipo_chocolate == "trufa":
            return Trufa(peso, sabor, relleno)
        else:
            raise ValueError("Tipo de chocolate no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocolateriaService:
    def __init__(self):
        self.factory = Chocolateria()

    def add_chocolate(self, data):
        tipo_chocolate = data.get("tipo_chocolate", None)
        peso = data.get("peso", None)
        sabor = data.get("sabor", None)
        relleno = data.get("relleno", None)

        chocolate = self.factory.create_chocolate(
            tipo_chocolate, peso, sabor, relleno
        )
        
        if not chocolates:
            id = 1
        else:
            id = max(chocolates.keys())+1
            
        chocolates[id] = chocolate
        return chocolate
    
        

    def list_chocolate(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in chocolates:
            chocolate = chocolates[chocolate_id]
            peso = data.get("peso", None)
            sabor = data.get("sabor", None)
            relleno = data.get("relleno", None)
            if peso:
                chocolate.peso = peso
            if sabor:
                chocolate.sabor = sabor
            if chocolate.tipo_chocolate!="tableta" and relleno:
                chocolate.relleno = relleno
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "Vehículo eliminado"}
        else:
            return None


class ChocolateriaRequestHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args, **kwargs):
        self.chocolateria_service = ChocolateriaService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolateria_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolateria_service.list_chocolate()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            vehicle_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolateria_service.update_chocolate(vehicle_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.chocolateria_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateriaRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()