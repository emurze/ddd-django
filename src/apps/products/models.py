from autoslug import AutoSlugField
from django.db import models

from seedwork.models import AggregateRoot


class Product(AggregateRoot):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, db_index=True, populate_from="title")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
