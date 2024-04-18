from flask import Flask, request, jsonify

app = Flask(__name__)

def count_vowels(cadena, vocal):
    c=0
    for character in cadena:
        if character == vocal:
            c=c+1
    
    return c

@app.route('/')
def hello_world():
    return 'Hola, mundo'


@app.route("/saludar", methods=['GET'])
def saludar():
    nombre=request.args.get("nombre")
    if not nombre:
        return(
            jsonify({"error":"Se requiere un nombre en los parametros de la URL"}),400,
        )
    return jsonify({"mensaje": f"!Hola, {nombre}!"})


@app.route("/sumar", methods=['GET'])
def sumar():
    num1=request.args.get("num1")
    num2=request.args.get("num2")
    if not num1 or not num2:
        return(
            jsonify({"error":"Falta un parametro(s)"}),400,
        )
    num1=int(num1)
    num2=int(num2)
    return jsonify({"suma": f"{num1+num2}"})


@app.route("/palindromo", methods=['GET'])
def pal():
    pal=request.args.get("cadena")
    if not pal:
        return(
            jsonify({"error":"Falta la cadena"}),400,
        )
    if pal == pal[::-1]:
       return jsonify({"palindromo": "palindromo"})
    else:
        return jsonify({"palindromo": "no palindromo"})

@app.route("/contar", methods=['GET'])
def contar():
    pal=request.args.get("cadena")
    vocal=request.args.get("vocal")
    if not pal or not vocal:
        return(
            jsonify({"error":"Falta un parametro(s)"}),400,
        )
    return jsonify({"contar": f"{count_vowels(pal,vocal)}"})


if __name__=='__main__':
    app.run()