from server.models.base_request import BaseRequest
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CredentialModel:
    web_address: str = field(default="")
    username: str = field(default="", repr=False)
    password: str = field(default="", repr=False)
    created_at: str = field(default=datetime.utcnow().isoformat())
    last_modified: str = field(default=datetime.utcnow().isoformat())

    def getDocument(self):
        return self.__dict__


class CredentRequest(BaseRequest):
    web_address: str
    username: str
    password: str

    def __init__(self, req_pars: dict):
        super().__init__(req_pars)
    
    def getCredential(self) -> CredentialModel:
        credential = CredentialModel()
        credential.web_address = self.data["web_address"]
        credential.username = self.data["username"]
        credential.password = self.data["password"]
        return credential
