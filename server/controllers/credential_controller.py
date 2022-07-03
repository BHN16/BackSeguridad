from flask import Blueprint, request
from ..services import credential_service
from ..models.credential_model import CredentRequest, EditCredRequest
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
    if not request.json.get('id'): 
        err_msg = {"error": "Bad credential request params" }
        return response(err_msg, 400)
    
    cred_id = request.json["id"]
    cred = credential_service.findByCredId(user_id, cred_id)
    
    if cred == None:
        return response({"msg": "Resource not found"}, 404)
    return response(cred, 200)


@cred_mod.route("/cred/", methods=["POST"])
@jwt.jwt_required()
def create_credential():
    user_id = str(jwt.current_user)
    cred_req = CredentRequest(request.json)

    if cred_req.getObject() == None:
        err_msg = {"error": "Bad credential request params" }
        return response(err_msg, 400)
    
    res = credential_service.createCredential(user_id, cred_req)

    if not res:
        return response({"msg": "Can't resolve operation"}, 400)
    return response({"Created": res}, 200)


@cred_mod.route("/cred/", methods=["PUT"])
@jwt.jwt_required()
def update_credential():
    user_id = str(jwt.current_user)
    edit_cred_req = EditCredRequest(request.json)

    if edit_cred_req.getObject() == None:
        err_msg = {"error": "Bad credential request params" }
        return response(err_msg, 400)
    
    cred_id = request.json["id"]
    cred = edit_cred_req.data
    print(cred)
    result = credential_service.editCredential(user_id, cred)

    if result == None:
        return response({"msg": "Resource not found"}, 404)
    return response({"msg": f"Updated {result}"}, 200)


@cred_mod.route("/cred/", methods=["DELETE"])
@jwt.jwt_required()
def delete_credential():
    user_id = str(jwt.current_user)
    if not request.json.get('id'): 
        err_msg = {"error": "Bad credential request params" }
        return response(err_msg, 400)
    
    cred_id = request.json["id"]
    result = credential_service.delete(user_id, cred_id)

    if not result:
        return response({"msg": "Resource not found"}, 404)
    return response({"msg": f"Deleted {result}"}, 200)
