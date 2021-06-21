from django.conf import settings
from django.db import models


class Entry(models.Model):
    "Generated Model"
    body = models.TextField()
    title = models.TextField(
        null=True,
        blank=True,
    )
