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
    try: return cred["credentials"][0]
    except: return None


def findByWebsite(user_id: str, web: str):
    filter = ("website", web)
    cred = findOne(user_id, filter)
    return cred


def findByCredId(user_id: str, cred_id: str):
    filter = ("id", cred_id)
    cred = findOne(user_id, filter)
    return cred


def create(user_id: str, cred: dict):
    if not valid_id(user_id): return None
    result = users_db.update_one(
        { "_id": ObjectId(user_id) },
        { "$push": { "credentials": cred } })
    return result.modified_count


def createCredential(user_id: str, cred_req: CredentRequest):
    credential: CredentialModel = cred_req.getCredential()

    valid = create(user_id, credential.getDocument())
    
    if not valid: return None
    return credential.getDocument()


def editCredential(user_id: str, cred: dict):
    if not valid_id(user_id): return None
    result = users_db.update_one(
        { "_id": ObjectId(user_id) },
        { "$set": { "credentials.$[elem]": cred } },
        array_filters=[ { "elem.id": {"$eq": cred["id"]} } ],
        upsert=False)
    return result.modified_count


# Delete by credential id
def delete(user_id: str, cred_id: str):
    if not valid_id(user_id): return None
    result = users_db.update_one(
        { "_id": ObjectId(user_id) },
        { "$pull": { "credentials": {"id": cred_id} } })
    return result.modified_count
