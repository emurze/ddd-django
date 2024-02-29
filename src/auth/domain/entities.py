from datetime import datetime
from typing import Optional

from shared.domain.model import Model


class Client(Model):
    id: int
    email: str
    username: str
    password: str
    first_name: str
    last_name: str
    description: Optional[str] = None

    # Name Business Rule, implement in Infrastructure
    date_joined: datetime
    last_login: Optional[datetime] = None

    is_staff: bool = False
    is_active: bool = True

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Client):
            return False
        return self.id == other.id

    def to_inactive(self) -> None:
        self.is_active = False
