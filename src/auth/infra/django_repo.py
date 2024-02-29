from dataclasses import dataclass, field

from auth.application.ports import IClientRepository
from auth.domain.entities import Client
from auth.infra.db_models import ClientModel


@dataclass(frozen=True, slots=True)
class DjangoClientRepository(IClientRepository):
    seen: set = field(default_factory=set)

    def add(self, **kw):
        client = ClientModel.objects.create(**kw)
        self.seen.add(client.to_domain())

    def update_from_domain(self, model: Client) -> None:
        ClientModel.update_from_domain(model)

    def get(self, **kw) -> Client | int:
        model = ClientModel.objects.filter(**kw).first()

        if model is not None:
            return model.to_domain()

        return 1

    def list(self) -> list[Client]:
        return [b.to_domain() for b in ClientModel.objects.all()]
