from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from shared.domain.model import Model


class AddClientInputDto(BaseModel):
    email: str
    username: str
    password: str
    first_name: str
    last_name: str
    description: Optional[str]


class AddClientOutputDto(Model):
    id: int
    email: str
    username: str
    password: str
    first_name: str
    last_name: str
    description: Optional[str]
    date_joined: Optional[datetime]
    last_login: Optional[datetime]
    is_staff: bool
    is_active: bool
