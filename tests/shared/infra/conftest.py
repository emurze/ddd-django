import pytest

from auth.application.ports.driven import IAuthUnitOfWork
from auth.infra.repos.django import DjangoClientRepository
from auth.infra.uow.django import DjangoAuthUnitOfWork


client_dict = {
    "email": "fwe@gmail.com",
    "username": "hello",
    "password": "12345678",
    "first_name": "first name",
    "last_name": "last name",
}


@pytest.fixture
def uow() -> IAuthUnitOfWork:
    return DjangoAuthUnitOfWork(
        clients=DjangoClientRepository(),
    )
