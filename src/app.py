import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Instancia de la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Miembros iniciales
initial_members = [
    {"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
    {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
    {"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
]

# Agregar los miembros iniciales
for member in initial_members:
    jackson_family.add_member(member)

# Manejo de errores
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generar el sitemap con los endpoints disponibles
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

# Obtener un solo miembro por ID
@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

# crear un nuevo miembro
@app.route('/member', methods=['POST'])
def create_member():
    new_member = request.json
    if not new_member or "first_name" not in new_member or "age" not in new_member:
        return jsonify({"error": "Invalid member data"}), 400
    
    added_member = jackson_family.add_member(new_member)
    return jsonify(added_member), 200

# eliminar un miembro por ID
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_single_member(id):
    if jackson_family.delete_member(id):
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
