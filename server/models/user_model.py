from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

@dataclass
class UserModel:
    username: str = field(default="")
    email: str = field(default="")
    password: str = field(default="", repr=False)
    created_at: str = field(default=datetime.utcnow().isoformat())

    def getDocument(self):
        return self.__dict__
