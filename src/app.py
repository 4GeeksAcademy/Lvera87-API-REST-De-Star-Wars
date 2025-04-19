"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Manejar y serializar errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generar sitemap con todos los endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# -----------------------------------------------------------------------------------
# A partir de aquí se crean los endpoints de la API
# -----------------------------------------------------------------------------------

# Método GET para mostrar todos los usuarios---------------------------------------------------------------------------
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_serialized = list(map(lambda x: x.serialize(), users))
    return jsonify(users_serialized), 200

# Método GET para mostrar un usuario específico por ID------------------------------------------------------------------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": "User not found"}), 404
    return jsonify(user.serialize()), 200

# Método POST para crear un nuevo usuario-------------------------------------------------------------------------------
@app.route('/users', methods=['POST'])
def create_user():
    body = request.get_json()# estos almacena la informacion enviada desde el frontend

    if not body:
        return jsonify({"msg": "Request body is empty"}), 400
    if "email" not in body or "first_name" not in body or "last_name" not in body or "password" not in body:
        return jsonify({"msg": "Missing required fields"}), 400

    user = User(
        email=body["email"],
        first_name=body["first_name"],
        last_name=body["last_name"],
        is_active=body.get("is_active", True),
        password=body.get['password'],
        subscription_date=body.get("subscription_date")
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201

# Método PUT para modificar un usuario existente------------------------------------------------------------------------
@app.route('/users/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": "User not found"}), 404

    body = request.get_json()
    if not body:
        return jsonify({"msg": "Request body is empty"}), 400
    
    user.first_name = body["first_name"]
    user.is_active = body["is_active"]
    user.last_name = body["last_name"]

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"msg": "Database error", "error": str(e)}), 500

    return jsonify({"msg": "User updated successfully", "user": user.serialize()}), 200

# Método DELETE para eliminar un usuario--------------------------------------------------------------------------------
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": "User not found"}), 404

    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        return jsonify({"msg": "Database error", "error": str(e)}), 500

    return jsonify({"msg": "User deleted"}), 200

# -----------------------------------------------------------------------------------
# A partir de aquí se crean los endpoints del modelo Planet
# -----------------------------------------------------------------------------------
# Método GET para mostrar todos los Planetas---------------------------------------------------------------------------
@app.route('/users', methods=['GET'])
def get_Planets():
    users = User.query.all()
    users_serialized = list(map(lambda x: x.serialize(), users))
    return jsonify(users_serialized), 200





















# Este código sólo corre si `$ python src/app.py` es ejecutado
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)