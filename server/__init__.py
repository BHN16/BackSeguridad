from flask import Flask, jsonify, request
from .extensions import mongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pass_manager"

mongo.init_app(app)

# import controllers
from .controllers.init_controller import inital
from .controllers.auth_controller import auth

app.register_blueprint(inital)
app.register_blueprint(auth)
