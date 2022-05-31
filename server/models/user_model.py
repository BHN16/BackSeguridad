from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class UserModel:
    username: str = field(default="")
    email: str = field(default="")
    password: str = field(default="", repr=False)
    created_at: str = field(default=datetime.utcnow().isoformat())

    def getModel(self):
        return self.__dict__
