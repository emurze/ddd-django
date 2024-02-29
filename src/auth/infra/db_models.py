from django.contrib.auth.models import AbstractUser
from django.db import models

from auth.domain.entities import Client


class ClientModel(AbstractUser):
    description = models.TextField(
        null=True,
        verbose_name='Description',
        max_length=120,
    )

    class Meta:
        db_table = "client"
        app_label = 'apps'

    @classmethod
    def update_from_domain(cls, client: Client) -> None:
        try:
            item = cls.objects.get(id=client.id)
        except cls.DoesNotExist:
            item = cls(id=client.id)

        client_dict = client.as_dict()
        for key, value in client_dict.items():
            setattr(item, key, value)

        item.save()
        # b.allocation_set.set(
        #     Allocation.from_domain(l, b)
        #     for l in batch._allocations
        # )

    def to_domain(self) -> Client:
        # b._allocations = set(
        #     a.line.to_domain()
        #     for a in self.allocation_set.all()
        # )
        return Client.model_validate(self)
