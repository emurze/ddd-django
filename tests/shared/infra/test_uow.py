import pytest

from auth.application.ports.driven import IAuthUnitOfWork
from tests.shared.infra.conftest import client_dict


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_can_commit_client(uow: IAuthUnitOfWork) -> None:
    with uow:
        uow.clients.add(**client_dict)
        uow.commit()

    with uow:
        clients = uow.clients.list()

        assert len(clients) == 1
        assert all(
            [getattr(clients[0], key) == val
             for key, val in (client_dict | {"id": 1}).items()]
        )


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_can_rollback_client(uow: IAuthUnitOfWork) -> None:
    with uow:
        uow.clients.add(**client_dict)

    with uow:
        clients = uow.clients.list()
        assert len(clients) == 0


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_can_update_client(uow: IAuthUnitOfWork) -> None:
    with uow:
        uow.clients.add(**client_dict)
        uow.commit()

    with uow:
        client = uow.clients.get(id=1)
        client.username = "lerka.com"
        print(client)


# @pytest.mark.django_db(transaction=True, reset_sequences=True)
# def test_can_rollback_commit_pipeline(uow: IAuthUnitOfWork) -> None:
#     # ROLLBACK
#     with uow:
#         uow.clients.add(**client_dict)
#
#     with uow:
#         assert len(uow.clients.list()) == 0
#
#     # COMMIT
#     with uow:
#         uow.clients.add(**client_dict)
#         uow.commit()
#
#     with uow:
#         assert len(uow.clients.list()) == 1
#
#     # ROLLBACK
#     with uow:
#         uow.clients.add(**client_dict | {"username": "1"})
#
#     with uow:
#         assert len(uow.clients.list()) == 1
#
#     # ROLLBACK
#     with uow:
#         uow.clients.add(**client_dict | {"username": "1"})
#
#     with uow:
#         assert len(uow.clients.list()) == 1
#
#     # COMMIT
#     with uow:
#         uow.clients.add(**client_dict | {"username": "1"})
#         uow.commit()
#
#     with uow:
#         assert len(uow.clients.list()) == 2
#
#     # COMMIT
#     with uow:
#         uow.clients.add(**client_dict | {"username": "2"})
#         uow.commit()
#
#     with uow:
#         assert len(uow.clients.list()) == 3
#
#     # COMMIT
#     with uow:
#         client = uow.clients.get(id=2)
#         client.is_active = True
#
#     with uow:
#         assert len(uow.clients.list()) == 3
