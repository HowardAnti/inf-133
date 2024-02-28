from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
 

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000",
    action="http://localhost:8000",
    namespace="http://localhost:8000",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"Saludo": str},
    args={"nombre": str}
)

server = HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher = dispatcher
print("Servidor Sopa iniciado en ")
server.serve_forever()


