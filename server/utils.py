from werkzeug.security import generate_password_hash, check_password_hash
from flask import make_response
from bson import json_util
import os

def genSalt():
    return os.urandom(16)

def generate_password(pwd: str):
    return generate_password_hash(pwd, method='pbkdf2:sha256:10')

def check_password(hashed_pwd: str, _pwd: str):
    return check_password_hash(hashed_pwd, _pwd)

def response(msg: object, code: int):
    try: res = json_util.dumps(msg)
    except: res = json_util.dumps(msg.__dict__)
    res = make_response(res, code)
    res.headers["content-type"] = "application/json"
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res