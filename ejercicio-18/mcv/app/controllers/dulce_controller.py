from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from views.dulce_view import render_dulce_list, render_dulce_detail
from flask_jwt_extended import  verify_jwt_in_request, get_jwt_identity
from functools import wraps
from utils.decorator import jwt_required, roles_required

# Crear un blueprint para el controlador de animales
dulce_bp = Blueprint("dulce", __name__)


# Ruta para obtener la lista de animales
@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required 
@roles_required(roles=["admin", "user"])
def get_libros():
    dulces = Dulce.get_all()
    return jsonify(render_dulce_list(dulces)) 


# Ruta para obtener un animal específico por su ID
@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulce(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "dulce no encontrado"}), 404


# Ruta para crear un nuevo animal
@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_dulce():
    data = request.json
    marca = data.get("marca")
    peso = data.get("peso")
    sabor = data.get("sabor")
    origen = data.get("origen")

    # Validación simple de datos de entrada
    if not marca or not peso or sabor is None or origen is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo animal y guardarlo en la base de datos
    libro = Dulce(marca=marca, peso=peso, sabor=sabor, origen=origen)
    libro.save()

    return jsonify(render_dulce_detail(libro)), 201


# Ruta para actualizar un animal existente
@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_dulce(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    data = request.json
    marca = data.get("marca")
    peso = data.get("peso")
    sabor = data.get("sabor")
    origen = data.get("origen")

    # Actualizar los datos del animal
    dulce.update(marca=marca, peso=peso, sabor=sabor, origen=origen)

    return jsonify(render_dulce_detail(dulce))
 

# Ruta para eliminar un animal existente
@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_dulce(id):
    dulce= Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    # Eliminar el animal de la base de datos
    dulce.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204