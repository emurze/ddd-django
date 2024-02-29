from auth.application.ports.driven import IAuthUnitOfWork
from auth.application.ports.driving import IAddClientUseCase
from auth.application.usecases.add_client import AddClientUseCase
from auth.infra.repos.django import DjangoClientRepository
from auth.infra.uow.django import DjangoAuthUnitOfWork


def get_uow() -> IAuthUnitOfWork:
    return DjangoAuthUnitOfWork(
        clients=DjangoClientRepository(),
    )


def add_client_uc_factory() -> IAddClientUseCase:
    return AddClientUseCase(uow=get_uow())
