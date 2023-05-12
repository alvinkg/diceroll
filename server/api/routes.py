from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required
from random import randint
from extensions import jwt

# instance of Blueprint api
api = Blueprint('api', __name__)

@api.route('/diceroll', methods=['GET'])
@jwt_required()
def generate():
    
    return jsonify(message='success', dice_roll=randint(1,6)),201
