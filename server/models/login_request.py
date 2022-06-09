# Model for incoming user signup requests

import email
from server.models.user_model import UserModel
from ..models.base_request import BaseRequest

class LoginRequest(BaseRequest):
    email: str
    password: str

    def __init__(self, req_pars: dict):
        super().__init__(req_pars)
    
    def getEmail(self) -> str:
        return self.data["email"]
    
    def getPassword(self) -> str:
        return self.data["password"]
