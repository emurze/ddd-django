from datetime import datetime

import pytest

from auth.application.ports import IAuthUnitOfWork
from auth.domain.entities import Client


class TestClientModel:
    @pytest.mark.django_db(transaction=True, reset_sequences=True)
    def test_can_create_client(self, uow: IAuthUnitOfWork) -> None:
        with uow:
            client_dict = {
                "email": "fwe@gmail.com",
                "username": "hello",
                "password": "12345678",
                "first_name": "first name",
                "last_name": "last name",
            }
            uow.clients.add(**client_dict)
            # uow.commit()

        with uow:
            print(uow.clients.list())
