from flask import Blueprint, request
from ..services import credential_service
from ..models.credential_model import CredentRequest
from ..services import jwt_service as jwt
from ..utils import response

cred_mod = Blueprint("credential", __name__)


@cred_mod.route("/creds/")
@jwt.jwt_required()
def get_credentials():
    user_id = str(jwt.current_user)
    creds = credential_service.findAll(user_id)

    if creds == None:
        return response({"msg": "Resource not found"}, 404)

    return response(creds, 200)


@cred_mod.route("/cred/")
@jwt.jwt_required()
def get_credential():
    user_id = str(jwt.current_user)
    web = request.json["website"]

    cred = credential_service.findByWebsite(user_id, web)
    
    if cred == None:
        return response({"msg": "Resource not found"}, 404)
    return response(cred, 200)


@cred_mod.route("/cred/", methods=["POST"])
@jwt.jwt_required()
def create_credential():
    user_id = str(jwt.current_user)
    cred_req = CredentRequest(request.json)

    if cred_req.getObject() == None:
        err_msg = {"error": "Bad credential resquest params" }
        return response(err_msg, 400)
    
    credential = cred_req.getCredential()
    res = credential_service.create(user_id, credential.getDocument())

    if not res:
        return response({"msg": "Can't resolve operation"}, 400)
    return response({"Created": res}, 200)


@cred_mod.route("/cred/", methods=["DELETE"])
@jwt.jwt_required()
def delete_credential():
    user_id = str(jwt.current_user)
    web = request.json["website"]

    result = credential_service.delete(user_id, web)

    if not result:
        return response({"msg": "Resource not found"}, 404)
    return response({"msg": f"Deleted {result}"}, 200)
