import pytest

from clients.infra import Client


class TestClientModel:
    @pytest.mark.django_db(transaction=True, reset_sequences=True)
    def test_can_create_client(self) -> None:
        client = Client(
            id=1,
            username="client",
            first_name="first name",
            last_name="last name",
            email="example@gmail.com",
            description="Cool client",
        )
        client.set_password("12345678")
        client.full_clean()
        client.save()
