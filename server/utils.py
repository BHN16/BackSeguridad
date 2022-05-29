from cryptography.hazmat.primitives import hashes

def hash(msg: str):
	digest = hashes.Hash(hashes.SHA1())
	digest.update(msg.encode("unicode_escape"))
	return digest.finalize().hex()

def iterativeHash(msg: str, n_iter: int = 5):
    hashed = msg
    for i in range(n_iter):
        hashed = hash(hashed)
        print(hashed)
    return hashed

def hashPwdAndSalt(pwd: str, salt: str):
    pt = salt +""+pwd + ":" + salt
    hashed_pwd = iterativeHash(pt)
    return hashed_pwd