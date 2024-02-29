from dataclasses import dataclass, fields
from typing import Self

from django.db import transaction

from auth.application.ports.driven import IClientRepository, IAuthUnitOfWork


@dataclass(frozen=True, slots=True)
class DjangoAuthUnitOfWork(IAuthUnitOfWork):
    clients: IClientRepository

    def __enter__(self) -> Self:
        transaction.set_autocommit(False)
        return self

    def __exit__(self, *args) -> None:
        self.rollback()
        transaction.set_autocommit(True)

    def commit(self) -> None:
        transaction.commit()

    def rollback(self) -> None:
        transaction.rollback()
