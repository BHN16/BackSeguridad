from bson import ObjectId
from ..models.user_model import UserModel
from ..models.signup_request import SignupRequest
from ..extensions import mongo
from ..utils import hashPwdAndSalt

users_db = mongo.db.users
attrs = ['username', 'email']


def findAll():
    return users_db.find()


def findOne(user_id: str):
    filter = {"_id": ObjectId(user_id)}
    return users_db.find_one(filter)


def create(user: dict):
    return users_db.insert_one(user)


def createUser(signup: SignupRequest):
    user: UserModel = signup.getUser()

    hashedPwd = hashPwdAndSalt(user.password, "asdf")
    user.password = hashedPwd

    create(user.getDocument())
    return user


def delete(user_id: str):
    filter = {"_id": ObjectId(user_id)}
    result = users_db.delete_one(filter)
    return result.deleted_count
