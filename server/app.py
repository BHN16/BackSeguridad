from flask import Flask, jsonify, request
from extensions import mongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pass_manager"

mongo.init_app(app)

from controllers.auth_controller import auth

app.register_blueprint(auth)


@app.route("/")
def hello_world():
    return {"message": "Server is working"}


if __name__ == "__main__":
    app.run(debug=True)
