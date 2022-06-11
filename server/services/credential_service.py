from server.services import user_service
from ..models.credential_model import CredentialModel, CredentRequest
from ..utils import valid_id, ObjectId
from ..extensions import mongo

users_db = mongo.db.users


def findAll(user_id: str):
    user = user_service.findOne(user_id)
    if not user: return None
    try: return user["credentials"]
    except: return list()


def findOne(user_id: str, filter: tuple):
    if not valid_id(user_id): return None
    key, value = filter
    cred = users_db.find_one(
        { "_id": ObjectId(user_id), f"credentials.{key}": value },
        { "credentials": {"$elemMatch": {key: value}} })
    return cred


def findByWebsite(user_id: str, web: str):
    filter = ("web_address", web)
    cred = findOne(user_id, filter)
    try: return cred["credentials"][0]
    except: return None


def create(user_id: str, cred: dict):
    if not valid_id(user_id): return None
    result = users_db.update_one(
        { "_id": ObjectId(user_id) },
        { "$push": { "credentials": cred } })
    return result.modified_count


def createCredential(user_id: str, credr: CredentRequest):
    credential: CredentialModel = credr.getCredential()

    valid = create(user_id, credential.getDocument())
    
    if not valid: return None
    return credential


# Delete by website
def delete(user_id: str, web: str):
    if not valid_id(user_id): return None
    filter = {"_id": ObjectId(user_id)}
    result = users_db.update_one(
        { "_id": ObjectId(user_id) },
        { "$pull": { "credentials": {"web_address": web} } })
    return result.modified_count
