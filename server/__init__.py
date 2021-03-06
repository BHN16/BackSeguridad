from flask import Flask, jsonify, request
from flask_cors import CORS
from .extensions import mongo, jwt

app = Flask(__name__)
CORS(app)

# Load MONGO_URI and JWT_SECRET_KEY
app.config.from_prefixed_env()

mongo.init_app(app)
jwt.init_app(app)

# import controllers
from .controllers.init_controller import inital
from .controllers.auth_controller import auth
#from .controllers.test_controller import test_mod
from .controllers.credential_controller import cred_mod

app.register_blueprint(inital)
app.register_blueprint(auth)
#app.register_blueprint(test_mod)
app.register_blueprint(cred_mod)
