import pytest

from auth.application.ports import IAuthUnitOfWork
from auth.infra.django_repo import DjangoClientRepository
from auth.infra.uow import DjangoAuthUnitOfWork


@pytest.fixture
def uow() -> IAuthUnitOfWork:
    return DjangoAuthUnitOfWork(
        clients=DjangoClientRepository(),
    )
