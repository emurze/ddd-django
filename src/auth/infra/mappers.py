from auth.domain.entities import Client
from auth.infra.db_models import ClientModel


class ClientMapper:
    def __init__(self) -> None:
        """Setup another mappers"""

    @staticmethod
    def to_entity(instance: ClientModel) -> Client:
        return Client(
            id=instance.id,
            email=instance.email,
            username=instance.username,
            password=instance.password,
            first_name=instance.first_name,
            last_name=instance.last_name,
            description=instance.description,
            date_joined=instance.date_joined,
            last_login=instance.last_login,
            is_staff=instance.is_staff,
            is_active=instance.is_active,
        )

    @staticmethod
    def to_instance(entity: Client) -> ClientModel:
        return ClientModel(
            id=entity.id,
            email=entity.email,
            username=entity.username,
            password=entity.password,
            first_name=entity.first_name,
            last_name=entity.last_name,
            description=entity.description,
            date_joined=entity.date_joined,
            last_login=entity.last_login,
            is_staff=entity.is_staff,
            is_active=entity.is_active,
        )
