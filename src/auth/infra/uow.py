from collections.abc import Iterator
from dataclasses import dataclass
from typing import Self, Any

from django.db import transaction

from auth.application.ports import IAuthUnitOfWork, IClientRepository


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
        print([*self.repos])
        for repo in self.repos:
            for model in repo.seen:
                repo.update_from_domain(model)

        transaction.commit()

    def rollback(self) -> None:
        transaction.rollback()

    @property
    def repos(self) -> list:
        return [self.clients]
