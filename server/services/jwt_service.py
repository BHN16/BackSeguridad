from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from server.services import user_service
from ..extensions import jwt


# Takes user id as the identity when creating JWTs
"""@jwt.user_identity_loader
def user_identity_lookup(user):
    return str(user["_id"])
"""

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    #return user_service.findOne(identity)
    return identity


def generate_token(user: dict, delta=None):
    if not delta: delta = timedelta(minutes=1)
    id = str(user["_id"])
    token = create_access_token(identity=id, expires_delta=delta)
    return token
