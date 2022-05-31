# Model for incoming user signup requests

from ..models.base_request import BaseRequest

class SignupRequest(BaseRequest):
    username: str
    email: str
    password: str
    color: str

    def __init__(self, req_pars: dict):
        super().__init__(req_pars)

