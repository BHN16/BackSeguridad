from flask import Flask, jsonify, request
from flask_cors import CORS
from .extensions import mongo

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://security:5gLq2FBzxRi2hxb@datastore.4tmh1zo.mongodb.net/pass_manager?retryWrites=true&w=majority"

mongo.init_app(app)

# import controllers
from .controllers.init_controller import inital
from .controllers.auth_controller import auth
from .controllers.test_controller import test_mod

app.register_blueprint(inital)
app.register_blueprint(auth)
app.register_blueprint(test_mod)
