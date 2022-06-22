from flask import Blueprint, redirect, request, url_for

from ..models.login_request import LoginRequest
from ..models.signup_request import SignupRequest
from ..services.jwt_service import *
from ..services import user_service
from ..utils import response

auth = Blueprint('auth', __name__)


@auth.route("/auth", methods=["POST"])
def signup_user():
    user_req = SignupRequest(request.json)
    
    if user_req.getObject() == None:
        err_msg = {"Error": "Bad signup resquest params" }
        return response(err_msg, 400)

    user_res = user_service.createUser(user_req)
    return response(user_res, 200)


@auth.route("/login", methods=["POST"])
def login_user():
    login_req = LoginRequest(request.json)
    
    if login_req.getObject() == None:
        err_msg = {"error": "Bad login request params" }
        return response(err_msg, 400)

    user = user_service.validateUser(login_req)
    if not user:
        err_msg = {"error": "Invalid email or password" }
        return response(err_msg, 400)
    
    access_token = generate_token(user)

    res = {"username": user["username"], "token": access_token}
    return response(res, 200)
