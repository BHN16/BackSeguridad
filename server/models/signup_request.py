# Model for incoming user signup requests

from server.models.user_model import UserModel
from ..models.base_request import BaseRequest

class SignupRequest(BaseRequest):
    username: str
    email: str
    password: str
    color: str

    def __init__(self, req_pars: dict):
        super().__init__(req_pars)
    
    def getUser(self) -> UserModel:
        user = UserModel()
        user.username = self.data["username"]
        user.email = self.data["email"]
        user.password = self.data["password"]
        return user
