from dataclasses import dataclass, field

from auth.application.ports.driven import IClientRepository
from auth.domain.entities import Client
from auth.infra.db_models import ClientModel
from auth.infra.mappers import ClientMapper


@dataclass(frozen=True, slots=True)
class DjangoClientRepository(IClientRepository):
    mapper: ClientMapper = field(default_factory=lambda: ClientMapper())

    def add(self, **kw):
        instance = ClientModel.objects.create(**kw)
        return self.mapper.to_entity(instance)

    def delete(self, **kw):
        ClientModel.objects.filter(**kw).delete()

    def get(self, **kw) -> Client:
        return self.mapper.to_entity(ClientModel.objects.filter(**kw).first())

    def list(self) -> list[Client]:
        return [self.mapper.to_entity(c) for c in ClientModel.objects.all()]
