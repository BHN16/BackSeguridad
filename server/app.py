from flask import Flask, Response, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util
from utils import *

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pass_manager"

mongo = PyMongo(app)


@app.route("/")
def hello_world():
    return {"message": "Server is working"}


@app.route("/user", methods=["POST"])
def create_user():
    # process data
    username = request.json["username"]
    email = request.json["email"]
    pwd = request.json["password"]
    hashAndSalt = hash(pwd)
    color = request.json["color"]

    user = {
        "username": username,
        "email": email,
        "password": hashAndSalt,
        "color": color
    }

    if username and email and pwd and color:
        #save user
        _id = mongo.db.users.insert_one(user)
        
        # response
        res = json_util.dumps(user)
        return Response(res, mimetype="aplication/json")
    else:
        return {"msg": "Error"}


if __name__ == "__main__":
    app.run(debug=True)
