from flask import Blueprint, request
from ..models.signup_request import SignupRequest
from ..services import user_service
from ..utils import response

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route("/", methods=["POST"])
def signup_user():
    user_req = SignupRequest(request.json)
    
    if user_req.getObject() == None:
        err_msg = {"Error": "Bad signup resquest params" }
        return response(err_msg, 400)

    user_res = user_service.createUser(user_req)
    return response(user_res, 200)
