from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util, ObjectId
from flask import make_response
import os
import uuid

def genRandom(size: int = 16):
    return os.urandom(size)

def genUUID():
    return uuid.uuid4().hex

def valid_id(id):
    return ObjectId.is_valid(id)

def generate_password(pwd: str):
    return generate_password_hash(pwd, method='sha256')

def check_password(hashed_pwd: str, _pwd: str):
    return check_password_hash(hashed_pwd, _pwd)

def response(msg: object, code: int):
    try: res = json_util.dumps(msg)
    except: res = json_util.dumps(msg.__dict__)
    res = make_response(res, code)
    res.headers["content-type"] = "application/json"
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res