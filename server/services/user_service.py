from ..models.user_model import UserModel
from ..extensions import mongo
from ..utils import hashPwdAndSalt

users_db = mongo.db.users

def createUser(user_dict: dict):
    user = UserModel()

    hashedPwd = hashPwdAndSalt(user_dict["password"], "asdf")
    user.username = user_dict["username"]
    user.email = user_dict["email"]
    user.password = hashedPwd

    users_db.insert_one(user.getModel())

    return user
