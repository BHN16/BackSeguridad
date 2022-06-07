from flask import Blueprint, request
from ..services import user_service
from ..utils import response

test_mod = Blueprint("test", __name__)

@test_mod.route("/users")
def get_users():
    all_users = user_service.findAll()
    return response(all_users, 200)

@test_mod.route("/user/<id>")
def get_user(id):
    user = user_service.findOne(id)
    return response({"msg": "Recibido", "user": user}, 200)

@test_mod.route("/user", methods=["POST"])
def create_user():
    user = user_service.create(request.json)
    return response({"msg": "Recibido", "user": user}, 200)

@test_mod.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    deleted = user_service.delete(id)
    return response({"msg": "Recibido", "Deleted": deleted}, 200)
