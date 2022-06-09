from bson import ObjectId
from ..models.login_request import LoginRequest
from ..models.user_model import UserModel
from ..models.signup_request import SignupRequest
from ..extensions import mongo
from ..utils import generate_password, check_password

users_db = mongo.db.users
attrs = ['username', 'email']


def findAll():
    return users_db.find()


def findOne(user_id: str):
    if not ObjectId.is_valid(user_id): return None
    filter = {"_id": ObjectId(user_id)}
    return users_db.find_one(filter)


def findByEmail(user_email: str):
    filter = {"email": user_email}
    return users_db.find_one(filter)


def create(user: dict):
    return users_db.insert_one(user)


def createUser(signup: SignupRequest):
    user: UserModel = signup.getUser()

    hashedPwd = generate_password(user.password)
    user.password = hashedPwd

    create(user.getDocument())
    return user


def validateUser(login: LoginRequest):
    user = findByEmail(login.getEmail())
    if not user: return None

    if check_password(user["password"], login.getPassword()):
        return user
    return None


def delete(user_id: str):
    if not ObjectId.is_valid(user_id): return None
    filter = {"_id": ObjectId(user_id)}
    result = users_db.delete_one(filter)
    return result.deleted_count
