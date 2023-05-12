from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

# extensions is where we keep all our extensions

# instantiate an object of JWTManager
jwt = JWTManager()
# instantiate an instance of SQLAlchemy
db = SQLAlchemy()

 