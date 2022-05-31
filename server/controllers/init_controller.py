from flask import Blueprint
from ..utils import response

inital = Blueprint("init", __name__)

@inital.route("/")
def hello_world():
    return response({"message": "Server is working"}, 200)
