from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "Hola, {}!".format(nombre)

def sumaDosNumeros(number_a, number_b):
    return number_a+number_b

def cadenaPalidromo(cadena):
    return cadena==cadena[::-1]
    
    


dispatcher = SoapDispatcher(
    "sum-soap-dispatcher",
    location="http://localhost:8000",
    action="http://localhost:8000",
    namespace="http://localhost:8000",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str}
)

dispatcher.register_function(
    "SumaDosNumeros",
    sumaDosNumeros,
    returns={"sum": int},
    args={"number_a": int, "number_b": int}
)

dispatcher.register_function(
    "CadenaPalindromo",
    cadenaPalidromo,
    returns={"is_palindromo": bool},
    args={"cadena": str}
)

def main():
    try:
        server = HTTPServer(("0.0.0.0",8000),SOAPHandler)
        server.dispatcher = dispatcher
        print("Servidor SOAP iniciado en http://localhost:8000/")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor...")
        server.socket.close()
        
        
if __name__=="__main__":
    main()