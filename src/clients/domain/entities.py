from datetime import datetime

from shared.domain.model import Model


class Client(Model):
    id: int
    email: str
    username: str
    password: str
    first_name: str
    last_name: str
    description: str
    is_staff: bool
    is_active: bool
    date_joined: datetime
    last_login: datetime
