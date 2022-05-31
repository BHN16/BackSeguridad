from ..models.user_model import UserModel
from ..models.signup_request import SignupRequest
from ..extensions import mongo
from ..utils import hashPwdAndSalt

users_db = mongo.db.users

def createUser(signup: SignupRequest):
    user: UserModel = signup.getUser()

    hashedPwd = hashPwdAndSalt(user.password, "asdf")
    user.password = hashedPwd

    users_db.insert_one(user.getDocument())
    return user
