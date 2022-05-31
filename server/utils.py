from cryptography.hazmat.primitives import hashes
from flask import Response
from bson import json_util
import os

def genSalt():
    return os.urandom(16)

def hash(msg: str):
	digest = hashes.Hash(hashes.SHA1())
	digest.update(msg.encode("unicode_escape"))
	return digest.finalize().hex()

def iterativeHash(msg: str, n_iter: int = 5):
    hashed = msg
    for i in range(n_iter):
        hashed = hash(hashed)
    return hashed

def hashPwdAndSalt(pwd: str, salt: str):
    pt = salt +":"+pwd + ":" + salt
    hashed_pwd = iterativeHash(pt)
    return f"{salt}:{hashed_pwd}"

def response(msg: object, code: int):
    try: res = json_util.dumps(msg)
    except: res = json_util.dumps(msg.__dict__)
    return Response(res, mimetype="aplication/json", status=code)