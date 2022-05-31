from flask import Blueprint, request
from models.signup_request import SignupRequest
import services.user_service as userService
from utils import response

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route("/", methods=["POST"])
def signup_user():
    user_req = SignupRequest(request.json).getObject()
    if user_req == {}:
        err_msg = {"Error": "Bad signup resquest params" }
        return response(err_msg, 400)

    user = userService.createUser(user_req)
    return response(user, 200)
