from server.models.base_request import BaseRequest
from dataclasses import dataclass, field
from server.utils import genUUID, genRandom



@dataclass
class CredentialModel:
    id: str = field(default=genRandom(32))
    website: str = field(default="")
    username: str = field(default="")
    bytes: str = field(default="", repr=False)

    def getDocument(self):
        return self.__dict__


class CredentRequest(BaseRequest):
    web: str
    bytes: str
    username: str

    def __init__(self, req_pars: dict):
        super().__init__(req_pars)
    
    def getCredential(self, gen_id: bool= True) -> CredentialModel:
        credential = CredentialModel()
        if gen_id: credential.id = genUUID()
        credential.website = self.data["web"]
        credential.bytes = self.data["bytes"]
        credential.username = self.data["username"]
        return credential
