from django.contrib.auth.models import AbstractUser
from django.db import models


class ClientModel(AbstractUser):
    description = models.TextField(
        null=True,
        verbose_name='Description',
        max_length=120,
    )

    class Meta:
        db_table = "client"
        app_label = "app"
