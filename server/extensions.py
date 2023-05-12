from flask import Blueprint
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

# extensions is where we keep all our extensions
extensions = Blueprint('extensions',__name__)

# instantiate an object of JWTManager
jwt = JWTManager()
# instantiate an instance of SQLAlchemy
db = SQLAlchemy()

 